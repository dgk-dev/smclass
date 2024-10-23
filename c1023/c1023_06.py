from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import random
import os
import platform

# 크롬드라이버 경로 설정
chrome_driver_path = "C:\workspace\smclass\chromedriver.exe"  # 크롬드라이버의 경로를 직접 입력

# Windows 버전과 크롬 드라이버의 호환성을 확인
if platform.system() == "Windows":
    architecture = platform.architecture()[0]
    if architecture == "32bit" and "x64" in chrome_driver_path:
        print("32bit Windows에서 64bit ChromeDriver는 사용할 수 없습니다. 32bit용 ChromeDriver를 다운로드하세요.")
        exit()
    elif architecture == "64bit" and "32" in chrome_driver_path:
        print("64bit Windows에서 32bit ChromeDriver는 사용할 수 없습니다. 64bit용 ChromeDriver를 다운로드하세요.")
        exit()

# 경로 확인 제거
if not os.path.isfile(chrome_driver_path):
    print("The specified path to the ChromeDriver is not valid. Please check the path and try again.")
    chrome_driver_path = input("Enter the correct path to chromedriver: ")

url = "https://quotes.toscrape.com/"

# 크롬 옵션 설정 (브라우저가 자동으로 열리는 것을 방지할 수 있는 옵션 추가)
chrome_options = Options()
chrome_options.add_argument("--headless")  # 브라우저 UI를 표시하지 않음
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

# 크롬드라이버 서비스 설정
service = Service(chrome_driver_path)

# 크롬 브라우저 열기
browser = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 명언 페이지 이동
    browser.get(url)
    time.sleep(random.uniform(2, 4))

    # 첫 페이지의 모든 명언을 가져오기
    quotes = browser.find_elements(By.CLASS_NAME, "text")
    authors = browser.find_elements(By.CLASS_NAME, "author")

    # 명언과 저자 출력
    for quote, author in zip(quotes, authors):
        print(f"\"{quote.text}\" - {author.text}")

    # 다음 페이지로 이동 (예제: 두 페이지의 명언을 가져오기)
    next_button = browser.find_element(By.CLASS_NAME, "next")
    next_button.click()
    time.sleep(random.uniform(2, 4))

    # 두 번째 페이지의 모든 명언을 가져오기
    quotes = browser.find_elements(By.CLASS_NAME, "text")
    authors = browser.find_elements(By.CLASS_NAME, "author")

    # 명언과 저자 출력
    for quote, author in zip(quotes, authors):
        print(f"\"{quote.text}\" - {author.text}")

finally:
    # 브라우저 닫기
    browser.quit()
