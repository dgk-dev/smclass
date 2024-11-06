'''
employees 테이블에서 이름이 a가 포함되어 있는 이름 출력

'''

a =[
    (196, 'Christopher Olsen', 8000.0),
    (196, 'Christopher Olsen', 8000.0),
    (196, 'Christopher Olsen', 8000.0),
    (196, 'Christopher Olsen', 8000.0),
    (196, 'Christopher Olsen', 8000.0)
]

aa = []



import oracledb

# db연결 함수선언
def connections():
    try:
        conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
        print("db연결 : ",conn.version)
    except Exception as e: print("예외발생 : ",e)
    return conn


def titlePrint():
    titles = ['아이디','이름','국어','영어','수학','합계','평균','등수','등록일']
    for title in titles:
        print(title,end="\t")
    print()
    print("-"*80)

## sql developer 실행
conn = connections()

## sql창이 열림
cursor = conn.cursor()

search = input("[최소월급],[최대월급]").split(",")

# sql작성, 실행
# excute 뒤에는 dict, list, tuple 타입만 가능
sql = "SELECT emp_name, salary FROM employees WHERE salary >= :min and salary <= :max order by salary desc"
cursor.execute(
    sql,
     {'min': f'{search[0]}',
      'max': f'{search[1]}'})

rows = cursor.fetchall()

for row in rows:
    for i,r in enumerate(row):
        print(r, end="\t\t")
    print()


cursor.close()
conn.close()
print("데이터베이스 연결이 종료되었습니다.")

