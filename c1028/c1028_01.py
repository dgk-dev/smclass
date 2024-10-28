import oracledb

# oracle 연결
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")

# 연결확인
print(conn.version)

# sql실행창 오픈
cursor = conn.cursor()
sql = "select * from member"
cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
    for item in row:
        print(item, end="\t")
    print()






# 연결을 확인해야함
conn.close()