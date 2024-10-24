from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random
from selenium.webdriver.chrome.options import Options
import pyautogui

# 설정 및 브라우저 열기
url = "https://new.land.naver.com/complexes?ms=37.4592802,126.8930386,17&a=APT:PRE:ABYG:JGC&e=RETAIL"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# 팝업을 클릭하여 제거
pyautogui.moveTo(1270, 550)
time.sleep(1)
pyautogui.moveTo(1270, 480)
pyautogui.click()
time.sleep(1)

# 스크롤 다운 작업
pyautogui.moveTo(200, 800)
time.sleep(1)
prev_height = browser.execute_script("return document.body.scrollHeight")
print("초기 화면 높이 : ", prev_height)

while True:
    pyautogui.scroll(-prev_height)
    time.sleep(2)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    prev_height = curr_height
    print("현재 높이 : ", prev_height)

# BeautifulSoup을 사용하여 페이지 소스 파싱
soup = BeautifulSoup(browser.page_source, "lxml")

# HTML 파일로 저장 (디버깅용)
with open("naver.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())

# 저장된 HTML 파일 불러오기
with open("naver.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, 'lxml')

# 매물 정보 추출
items = soup.select(".item_area")

# 매매 및 전세 가격 정보 저장
sales_list = []
rent_list = []

for item in items:
    try:
        title = item.select_one(".title").get_text(strip=True)
        price_info = item.select_one(".price_line").get_text(strip=True)
        price_info = price_info.replace("억", "00000000").replace(",", "").replace("만원", "0000")

        # 매매 또는 전세 여부 판단 및 리스트에 추가
        if "매매" in price_info:
            price = int(price_info.replace("매매", ""))
            sales_list.append((title, price))
        elif "전세" in price_info:
            price = int(price_info.replace("전세", ""))
            rent_list.append((title, price))
    except Exception as e:
        print("Error while parsing item: ", e)

# 매매 가격이 낮은 순으로 정렬 후 상위 5개 출력
sales_list = sorted(sales_list, key=lambda x: x[1])
print("\n매매 가격이 낮은 5개 매물:")
for sale in sales_list[:5]:
    print(f"{sale[0]} - {sale[1]}만원")

# 전세 가격이 낮은 순으로 정렬 후 상위 5개 출력
rent_list = sorted(rent_list, key=lambda x: x[1])
print("\n전세 가격이 낮은 5개 매물:")
for rent in rent_list[:5]:
    print(f"{rent[0]} - {rent[1]}만원")

# 엔터키 입력 대기
input("엔터키 입력완료")

# 브라우저 종료
browser.quit()
