# 오라클 db에서는 타입 결정
# 문자형(숫자만) 타입 + 숫자와 사칙연산 됨.
# 파이썬에서 호출한 타입의 결과값이 어떻게 되는지 확인

import oracledb

def connects():
  user = 'ora_user'
  password = '1111'
  dsn = 'localhost:1521/xe'
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외처리 :",e)
  return conn

conn = connects()
cursor = conn.cursor()

# number, number, varchar2, varchar2
sql = "select * from chartable"
cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
  print(row)

print("검색완료")
conn.close()
  