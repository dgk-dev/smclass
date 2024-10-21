import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&q=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}

# 페이지 요청 및 상태 코드 확인
res = requests.get(url, headers=headers)
res.raise_for_status()

# BeautifulSoup 객체 생성
soup = BeautifulSoup(res.text, "lxml")

# 포스터 밑에 있는 영화 제목 정보 찾기 (다양한 구조 대응)
data = soup.find("c-flicking", attrs={"id": "mor_history_id_0"})
print(data.find("c-badge-text").next)
print(data.find("c-title").next)


# for idx, movie in enumerate(top_movie_elements):
#     print(f"{idx + 1}. {movie.get_text().strip()}")
