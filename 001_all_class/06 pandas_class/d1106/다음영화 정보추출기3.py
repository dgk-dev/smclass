import pandas as pd
from tabulate import tabulate

# CSV 파일 읽기
df = pd.read_csv("movie_data.csv")

# 통계 계산
max_audience = df["Audience"].max()
min_audience = df["Audience"].min()
mean_audience = df["Audience"].mean()

# 상위 5개, 하위 5개 영화 추출
top_5_movies = df.nlargest(5, "Audience")[["Title", "Audience", "Year"]]
bottom_5_movies = df.nsmallest(5, "Audience")[["Title", "Audience", "Year"]]

# 컬럼명 한글로 변경
column_names = {"Title": "영화제목", "Audience": "관객수", "Year": "개봉연도"}
top_5_movies = top_5_movies.rename(columns=column_names)
bottom_5_movies = bottom_5_movies.rename(columns=column_names)

# 관객수를 천 단위 쉼표가 있는 문자열로 변환
top_5_movies["관객수"] = top_5_movies["관객수"].apply(lambda x: f"{x:,}")
bottom_5_movies["관객수"] = bottom_5_movies["관객수"].apply(lambda x: f"{x:,}")

print("=" * 50)
print("영화 관객수 통계")
print("=" * 50)
print(f"최대 관객수: {max_audience:,}명")
print(f"최소 관객수: {min_audience:,}명")
print(f"평균 관객수: {mean_audience:,.0f}명")

print("\n" + "=" * 50)
print("관객수 TOP 5 영화")
print("=" * 50)
print(
    tabulate(
        top_5_movies,
        headers="keys",
        tablefmt="pretty",
        colalign=("left", "right", "right"),
    )
)

print("\n" + "=" * 50)
print("관객수 BOTTOM 5 영화")
print("=" * 50)
print(
    tabulate(
        bottom_5_movies,
        headers="keys",
        tablefmt="pretty",
        colalign=("left", "right", "right"),
    )
)
