from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
from bs4 import BeautifulSoup
import random

# 옵션 설정하기 (봇 탐지를 줄이기 위한 옵션)
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 열기
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# JavaScript로 자동화되지 않았음을 위장하기 위한 방법
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

# 브라우저 최대화
browser.maximize_window()

# URL 설정
url = 'https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=61&p='

# html 저장 및 조건에 맞는 상품 필터링하기
for i in range(1, 4):
    # 페이지로 이동
    browser.get(url + str(i))
    
    # 사람처럼 행동하기 위해 랜덤 대기 시간 추가
    time.sleep(random.uniform(4, 7))
    
    # BeautifulSoup 사용하여 페이지 파싱
    soup = BeautifulSoup(browser.page_source, "lxml")
    
    # 상품 정보 가져오기
    items = soup.find_all("div", class_="box__item-container")
    
    # 조건에 맞는 상품 필터링
    for item in items:
        try:
            satisfaction = float(item.select_one("span.text__rating").get_text().replace('%', ''))
            reviews = int(item.select_one("span.text__reviewcnt").get_text().replace('건', '').replace(',', ''))
            price = int(item.select_one("span.text__price").get_text().replace('원', '').replace(',', ''))
            
            if satisfaction >= 95 and reviews >= 100 and price <= 1500000:
                with open(f'gmarket_filtered_page_{i}.txt', 'a', encoding='utf-8') as f:
                    f.write(f"상품명: {item.select_one('span.text__item').get_text().strip()}\n")
                    f.write(f"만족도: {satisfaction}%\n")
                    f.write(f"리뷰 수: {reviews}\n")
                    f.write(f"가격: {price}원\n")
                    f.write(f"링크: {item.select_one('a.link__item').get('href')}\n\n")
        except AttributeError:
            # 일부 요소가 없을 경우 건너뜀
            continue

# 브라우저 닫기
browser.quit()
