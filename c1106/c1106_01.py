import oracledb
from datetime import datetime


def screen():
    print("\n[ 학생성적프로그램 ]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적검색")
    print("4. 학생성적정렬")
    print("5. 등수처리")
    print("0. 프로그램종료")
    choice = input("원하는 번호를 입력하세요.>> ")
    return choice


def connects():
    user = "ora_user"
    password = "1111"
    dsn = "localhost:1521/xe"
    try:
        conn = oracledb.connect(user=user, password=password, dsn=dsn)
    except Exception as e:
        print("예외발생 : ", e)
    return conn


def input_student(conn):
    cur = conn.cursor()

    # 마지막 번호 조회
    sql_max = "SELECT MAX(no) FROM students"
    cur.execute(sql_max)
    max_no = cur.fetchone()[0]
    new_no = 1 if max_no is None else max_no + 1

    name = input("학생 이름을 입력하세요: ")
    kor = int(input("국어 점수: "))
    eng = int(input("영어 점수: "))
    math = int(input("수학 점수: "))
    total = kor + eng + math
    avg = total / 3
    current_date = datetime.now().strftime("%y/%m/%d")

    sql = """
    INSERT INTO students (no, name, kor, eng, math, total, avg, rank, sdate)
    VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)
    """
    try:
        cur.execute(sql, (new_no, name, kor, eng, math, total, avg, 0, current_date))
        conn.commit()
        print("학생 성적이 입력되었습니다.")
    except Exception as e:
        print("입력 중 오류 발생:", e)
    finally:
        cur.close()


def print_students(conn):
    cur = conn.cursor()
    sql = "SELECT * FROM students ORDER BY no"
    try:
        cur.execute(sql)
        print("\n[ 전체 학생 성적 현황 ]")
        print("번호 이름   국어 영어 수학 총점   평균   등수  입력일")
        print("-" * 60)
        for student in cur:
            # None 값 처리
            no = student[0] if student[0] is not None else 0
            name = student[1] if student[1] is not None else ""
            kor = student[2] if student[2] is not None else 0
            eng = student[3] if student[3] is not None else 0
            math = student[4] if student[4] is not None else 0
            total = student[5] if student[5] is not None else 0
            avg = student[6] if student[6] is not None else 0
            rank = student[7] if student[7] is not None else 0
            sdate = student[8] if student[8] is not None else ""

            # 날짜 형식 변환 (YYYY-MM-DD HH:MI:SS -> YY/MM/DD)
            if sdate:
                try:
                    date_obj = datetime.strptime(str(sdate), "%Y-%m-%d %H:%M:%S")
                    sdate = date_obj.strftime("%y/%m/%d")
                except:
                    pass

            print(
                f"{no:<4d} {name:<8s} {kor:<4d} {eng:<4d} {math:<4d} {total:<6d} "
                f"{avg:<6.1f} {rank:<4d} {sdate}"
            )
    except Exception as e:
        print("조회 중 오류 발생:", e)
    finally:
        cur.close()


def search_student(conn):
    cur = conn.cursor()
    name = input("검색할 학생 이름을 입력하세요: ")
    sql = "SELECT * FROM students WHERE name LIKE :1"
    try:
        cur.execute(sql, (f"%{name}%",))
        print("\n[ 검색 결과 ]")
        print("번호 이름   국어 영어 수학 총점   평균   등수  입력일")
        print("-" * 60)
        for student in cur:
            print(
                f"{student[0]:<4d} {student[1]:<6s} {student[2]:<4d} {student[3]:<4d} "
                f"{student[4]:<4d} {student[5]:<6d} {student[6]:<6.1f} {student[7]:<4d} {student[8]}"
            )
    except Exception as e:
        print("검색 중 오류 발생:", e)
    finally:
        cur.close()


def sort_students(conn):
    cur = conn.cursor()
    print("\n정렬 방식 선택")
    print("1. 총점 높은 순")
    print("2. 총점 낮은 순")
    choice = input("선택: ")

    order = "DESC" if choice == "1" else "ASC"
    sql = f"SELECT * FROM students ORDER BY total {order}"

    try:
        cur.execute(sql)
        print("\n[ 정렬 결과 ]")
        print("번호 이름   국어 영어 수학 총점   평균   등수  입력일")
        print("-" * 60)
        for student in cur:
            print(
                f"{student[0]:<4d} {student[1]:<6s} {student[2]:<4d} {student[3]:<4d} "
                f"{student[4]:<4d} {student[5]:<6d} {student[6]:<6.1f} {student[7]:<4d} {student[8]}"
            )
    except Exception as e:
        print("정렬 중 오류 발생:", e)
    finally:
        cur.close()


def update_rank(conn):
    cur = conn.cursor()
    try:
        sql = """
        UPDATE students s1
        SET rank = (
            SELECT COUNT(*) + 1 
            FROM students s2 
            WHERE s2.total > s1.total
        )
        """
        cur.execute(sql)
        conn.commit()
        print("등수 처리가 완료되었습니다.")
    except Exception as e:
        print("등수 처리 중 오류 발생:", e)
    finally:
        cur.close()


def main():
    conn = connects()
    while True:
        choice = screen()
        if choice == "1":
            input_student(conn)
        elif choice == "2":
            print_students(conn)
        elif choice == "3":
            search_student(conn)
        elif choice == "4":
            sort_students(conn)
        elif choice == "5":
            update_rank(conn)
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")

    conn.close()


if __name__ == "__main__":
    main()
