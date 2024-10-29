import oracledb

## sql developer 실행
conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')

## sql창이 열림
cursor = conn.cursor()

# sql작성, 실행
sql = "select * from students"
cursor.execute(sql)

num = input("숫자를 입력하세요.")
n_list = num.split(",")


# sql = "select * from students where no in(:1,:2,:3)"
# cursor.execute(sql,n_list)
# # cursor.execute(sql,no1=num1,no2=num2,no3=num3)

rows = cursor.fetchall()
titles = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']
for title in titles:
    print(title,end="\t")
print()
print("-"*80)

for row in rows:
    for i,r in enumerate(row):
        if i == 1:
            print(f"{r:11s}",end="\t")
            continue
        if i==6:
            print(f"{r:.2f}", end="\t")
            continue
        if i == 8:
            print(r.strftime("%y-%m-%d"),end="\t")    
        else:
            print(r, end="\t")
    print()

cursor.close()
conn.close()
print("데이터베이스 연결이 종료되었습니다.")