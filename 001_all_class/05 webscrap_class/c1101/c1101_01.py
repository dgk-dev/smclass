import oracledb
import datetime

nowYear = datetime.datetime.now().year

def connects():
    user = "ora_user"
    password = "1111"
    dsn = "localhost:1521/xe"
    try:
        conn = oracledb.connect(user=user, password=password, dsn=dsn)
        return conn
    except Exception as e:
        print("데이터베이스 연결 실패:", e)
        return None

def member_count():
    conn = connects()
    if not conn:
        return (0, 0, "연결 실패")
    
    cursor = conn.cursor()
    sql = """
        SELECT COUNT(employees.emp_name) AS total_employees, 
               employees.department_id, 
               departments.department_name 
        FROM employees 
        JOIN departments ON employees.department_id = departments.department_id 
        WHERE employees.department_id = 50 
        GROUP BY departments.department_name, employees.department_id
    """
    try:
        cursor.execute(sql)
        row = cursor.fetchone()
        return row
    except Exception as e:
        print("쿼리 실행 실패:", e)
        return (0, 0, "쿼리 실패")
    finally:
        cursor.close()
        conn.close()

def login():
    id = input("아이디를 입력하세요.>> ")
    pw = input("비밀번호를 입력하세요.>> ")
    
    conn = connects()
    if not conn:
        return False
    
    cursor = conn.cursor()
    try:
        sql = "SELECT * FROM mem WHERE id=:1 AND pw=:2"
        cursor.execute(sql, (id, pw))
        row = cursor.fetchone()
        if row:
            print("로그인 성공!")
            return True
        else:
            print("아이디 또는 비밀번호가 일치하지 않습니다.")
            return False
    finally:
        cursor.close()
        conn.close()

def register():
    id = input("아이디를 입력하세요.>> ")
    pw = input("비밀번호를 입력하세요.>> ")
    name = input("이름을 입력하세요.>> ")
    birth = input("생일을 입력하세요.(예) 20020312)>> ")
    age = nowYear - int(birth[:4])
    gender = input("성별을 입력하세요.(Male,Female)>> ")
    hobby = input("취미를 입력하세요.>> ")
    
    conn = connects()
    if not conn:
        return
    
    cursor = conn.cursor()
    try:
        # 아이디 중복 체크
        sql = "SELECT id FROM mem WHERE id=:1"
        cursor.execute(sql, (id,))
        if cursor.fetchone():
            print("이미 존재하는 아이디입니다.")
            return
        
        # 회원가입 처리
        sql = "INSERT INTO mem(id, pw, name, age, birth, gender, hobby) VALUES(:1, :2, :3, :4, :5, :6, :7)"
        cursor.execute(sql, (id, pw, name, age, birth, gender, hobby))
        conn.commit()
        print("회원가입이 완료되었습니다.")
    except Exception as e:
        print("회원가입 실패:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def update_member():
    id = input("수정할 계정의 아이디를 입력하세요.>> ")
    conn = connects()
    if not conn:
        return
    
    cursor = conn.cursor()
    try:
        # 회원 정보 확인
        sql = "SELECT * FROM mem WHERE id=:1"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        if not row:
            print("존재하지 않는 아이디입니다.")
            return
        
        print("\n현재 정보:")
        print(f"취미: {row[6]}")
        
        # 정보 수정
        new_hobby = input("수정할 취미를 입력하세요.>> ")
        sql = "UPDATE mem SET hobby=:1 WHERE id=:2"
        cursor.execute(sql, (new_hobby, id))
        conn.commit()
        print("정보가 성공적으로 수정되었습니다.")
    except Exception as e:
        print("정보 수정 실패:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

# 메인 실행 코드
def main():
    while True:
        data = member_count()
        print(" [ 커뮤니티 ] ")
        print("1. 로그인")
        print("2. 회원가입")
        print("3. 회원정보수정")
        print("4. ")
        print("4. 종료")
        
        choice = input("원하는 번호를 입력하세요.>> ")
        
        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            update_member()
        elif choice == "4":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()