from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

url = "https://www.whatismybrowser.com/"
# 부동자 열기 (브라우저 창을 뜨지 않게 설정 및 유저로 인식되도록 설정)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 창을 뜨지 않게 설정
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')  # 자동화 탐지를 우회
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')  # 사용자 에이전트를 설정하여 일반 유저처럼 인식되도록 함

# WebDriver가 자동화된 브라우저임을 숨기기 위한 추가 설정
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

browser = webdriver.Chrome(options=options)  # chromedriver 경로를 명시적으로 추가해주는 것이 좋습니다.

# WebDriver가 자동화된 브라우저임을 JavaScript에서 감지하지 못하도록 설정
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        });
    """
})

# url 입력
browser.get(url)

# 자동시 로딩 대기
WebDriverWait(browser, 30).until(
    EC.presence_of_element_located((By.TAG_NAME, 'body'))
)

# 화면 캡처 저장하기
browser.save_screenshot('whatismybrowser_screenshot.png')

# BeautifulSoup을 이용하여 페이지 파싱
soup = BeautifulSoup(browser.page_source, "lxml")

# html 저장하기
with open('whatismybrowser.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

# 결과 출력 확인
print("페이지 소스가 저장되었습니다. 스크린샷도 저장되었습니다.")

# 브라우저 종료
browser.quit()
