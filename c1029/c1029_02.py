import oracledb

# 데이터베이스 연결 설정
try:
    conn = oracledb.connect(user='ora_user', password='1111', dsn='localhost:1521/xe')
    print("데이터베이스에 성공적으로 연결되었습니다.")
except oracledb.Error as e:
    print("데이터베이스 연결에 실패했습니다.", e)
    exit()

# 커서 생성 및 SQL 실행
try:
    cursor = conn.cursor()
    sql = "SELECT * FROM students"
    cursor.execute(sql)

    # 데이터 가져오기 및 출력
    rows = cursor.fetchall()
    titles = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수', '등록일']

    # 컬럼 제목 출력
    print("\t".join(titles))
    print("-" * 80)

    # 데이터 행 출력
    for row in rows:
        for i, r in enumerate(row):
            if i == 1:
                # 이름 컬럼은 문자열 포맷을 맞춰서 출력
                print(f"{r:11s}", end="\t")
            elif i == 6:
                # 평균 컬럼은 소수점 두 자리까지 출력
                print(f"{r:.2f}", end="\t")
            elif i == 8:
                # 등록일은 특정 형식으로 출력
                print(r.strftime("%y-%m-%d"), end="\t")
            else:
                print(r, end="\t")
        print()

except oracledb.Error as e:
    print("SQL 실행에 실패했습니다.", e)

# 리소스 정리
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("데이터베이스 연결이 종료되었습니다.")
