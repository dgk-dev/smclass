import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/index.htm"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}

# 페이지 요청 및 상태 코드 확인
res = requests.get(url, headers=headers)
res.raise_for_status()

# BeautifulSoup 객체 생성
soup = BeautifulSoup(res.text, "lxml")

# 이슈 리스트에서 영화 제목 및 이미지 정보 찾기
data = soup.find("li", {"class": "issue_list04"}).find_all("dl")

# 영화 제목 및 이미지 출력
for d in data:
    title_element = d.find("span", {"class": "title"})
    image_element = d.find("img")
    title = title_element.text.strip() if title_element else "제목 없음"
    image_url = image_element["src"] if image_element else "이미지 없음"
    print(f"제목: {title}, 이미지 URL: {image_url}")
