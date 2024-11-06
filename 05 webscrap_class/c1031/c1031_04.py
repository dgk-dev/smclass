### 입력한 달 이상의 입사한 사원을 출력하시오.

import oracledb

def connects():
  user="ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외발생 : ",e)  
  return conn

d_day = int(input("숫자를 입력하세요.>> "))
formatted_d_day = f"{d_day:02}"
print(formatted_d_day)

conn = connects()
cursor = conn.cursor()
sql = "select emp_name, hire_date from employees where substr(to_char(hire_date),4,2) >= :d_day"
cursor.execute(sql,d_day=formatted_d_day)
rows = cursor.fetchall()
print(rows)
