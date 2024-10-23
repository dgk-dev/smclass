import requests
from bs4 import BeautifulSoup
import csv
import time

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
try:
    res = requests.get(url, headers=headers, timeout=10)
    res.raise_for_status()  # 에러시 종료
except requests.exceptions.RequestException as e:
    print(f"요청 중 오류 발생: {e}")
    exit()

soup = BeautifulSoup(res.text, "lxml")

# 기준점
try:
    data = soup.select_one('#contentarea > div.box_type_l > table')
    if data is None:
        print("데이터를 찾지 못했습니다.")
        exit()
    stocks = data.select('tr')
    print(stocks)
except AttributeError as e:
    print(f"HTML 구조에서 데이터가 누락되었습니다: {e}")
    exit()

# 상단타이틀 리스트 내포를 이용해 코드 줄임
st_list = [st.text.strip() for st in stocks[0].select("th")]

sto_list = []
# 30개 주식정보를 csv파일로 저장하시오
for i in range(2, len(stocks)):
    cells = stocks[i].select("td")
    if len(cells) == len(st_list):
        sto_list.append([sto.text.strip().replace("\t", "").replace("\n", "") for sto in cells])

# 빈 항목 삭제는 리스트 컴프리헨션을 이용
sto_list = [item for item in sto_list if item != '']

# CSV 파일로 저장하기
with open('stock_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(st_list)  # 상단 타이틀 추가
    writer.writerows(sto_list)  # 주식 정보 추가

print(sto_list)
