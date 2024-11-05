# 학생성적프로그램
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적검색
# Students 테이블 사용해서
# 시퀀스 students_seq 생성
# 김유신,99,98,96 합계, 평균, 등수, 입력일

import oracledb

# 첫 메뉴
def screen():
    print("[ 학생성적프로그램 ]")
    print("1.학생성적입력")
    print("2.학생성적출력")
    print("3.학생성적검색")
    choice = input("원하는 번호를 입력하세요.>> ")
    return choice

# DB 연결
def connects():
    user='ora_user'
    password = '1111'
    dsn = 'localhost:1521/xe'
    try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
    except Exception as e: print("예외발생 : ",e)
    return conn

