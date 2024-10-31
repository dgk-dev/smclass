import random
import smtplib
import oracledb
from email.mime.text import MIMEText

def screen():
    print("[ 커뮤니티 ]")
    print("1.로그인")
    print("2.비밀번호 찾기")
    print("3.회원가입")
    print("4.프로그램 종료")
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

# 1. 로그인 함수선언
def memLogin():
    print("[ 로그인 ]")
    user_id = input("아이디를 입력하세요.>> ")
    user_pw = input("패스워드를 입력하세요.>> ")

    # db접속
    conn = connects()
    cursor = conn.cursor()
    sql = 'select * from member where id=:id and pw=:pw'
    cursor.execute(sql,id=user_id,pw=user_pw)
    
    # id와 pw가 일치하는 것을 불러옴
    row = cursor.fetchone()
    cursor.close()

    # id, pw가 모두 일치하는 row가 없으면 안내문, 있으면 로그인 성공
    if row == None:
        print("아이디 또는 패스워드가 일치하지 않습니다. 다시 입력하세요.")
        return

    print(f"로그인 성공! {row[2]}님 오늘도 좋은 하루 되세요.")
    print()

# 2. 비밀번호 찾기
def searchPassword():
    print("[ 비밀번호 찾기 ]")
    user_id = input("아이디를 입력하세요.>> ")

    # db 접속
    conn = connects()
    cursor = conn.cursor()

    # id가 있는 지 확인
    sql = 'select * from member where id=:id'
    cursor.execute(sql,id=user_id)
    row = cursor.fetchone()
    
    if row == None:
        print('아이디가 존재하지 않습니다. 다시 시도해주세요!')
        return

    input(f"{row[0]} 아이디가 존재합니다. 메일을 보내려면 enter를 입력하세요.")
    random_pw = emailSend(row[3])


    # 임시비밀번호를 update
    sql = "update member set pw=:pw where id=:id"
    cursor.execute(sql,pw=random_pw,id=user_id)
    conn.commit()

def randomPassword():
  a = random.randrange(0,10000) #0-9999
  ran_num = f"{a:04}"
  print("랜덤번호 : ",ran_num)
  return ran_num

# 메일발송 함수선언
def emailSend(email):
  #email 발송
  smtpName = "smtp.naver.com"
  smtpPort = 587

  sendEmail = "solicitor_@naver.com"
  pw = "BW3P42LDCG9E"
  recvEmail = email

  title = "제목 : [ 메일발송 ] 임시번호 발송"
  random_pw = randomPassword()
  content = f"임시비밀번호: "+random_pw
  print(content)
  
  # 설정
  msg = MIMEText(content)
  msg['Subject'] = title
  msg['From'] = sendEmail
  msg['To'] = recvEmail
  
  # 서버이름,서버포트
  s = smtplib.SMTP(smtpName,smtpPort)
  s.starttls()
  s.login(sendEmail,pw)
  s.sendmail(sendEmail,recvEmail,msg.as_string())
  s.quit()

  # 메일발송완료
  print("메일을 발송했습니다.")

  return random_pw


  