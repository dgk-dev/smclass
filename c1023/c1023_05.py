from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

# URL 설정
url_template = "https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&autoKeyword=&checkIn=2024-10-23&checkOut=2024-10-24&personal=2&freeForm=true&page={}"  # 페이지 넘버 추가

# Chrome 드라이버 설정
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# HTML 파일 저장 폴더 경로 설정
html_dir = 'smclass/c1023/'

# 1~5페이지에 대해 HTML 파일 저장 및 파싱
all_titles = []
all_rates = []
all_prices = []

for page in range(1, 6):
    # 각 페이지의 URL로 이동
    url = url_template.format(page)
    browser.get(url)

    # 페이지가 완전히 로드될 때까지 대기 (동적 로딩 처리)
    time.sleep(2)  # 혹은 WebDriverWait을 사용할 수 있습니다.

    # BeautifulSoup으로 파싱
    soup = BeautifulSoup(browser.page_source, "lxml")

    # HTML 파일로 저장
    html_filename = f'{html_dir}yeogi_page_{page}.html'
    with open(html_filename, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

    # 데이터 선택 및 추출
    data_div = soup.select_one("#__next > div > main > section > div.css-1qumol3")

    if data_div:
        titles = [title.text.strip().replace("\n", "") for title in data_div.select("a > div > div.css-1by0ap6 > div.css-b0qdn7 > div > div > div.css-8fn780 > h3")]
        rates = [rate.text.strip().replace("\n", "") for rate in data_div.select(".css-9ml4lz")]
        prices = [price.text.strip().replace("\n", "") for price in data_div.select("span.css-5r5920")]

        all_titles.extend(titles)
        all_rates.extend(rates)
        all_prices.extend(prices)

# 브라우저 종료
browser.quit()

# 평점 9.0 이상, 금액 120000원 이하인 숙소만 출력
for i in range(len(all_titles)):
    try:
        rate = float(all_rates[i])
        price = int(all_prices[i].replace(",", "").replace("원", ""))
        if rate >= 9.0 and price <= 120000:
            print(f"{all_titles[i]}의 평점은 {all_rates[i]}입니다.")
            print(f"가격은: {all_prices[i]}원 입니다.\n")
    except ValueError:
        # 평점이나 가격이 변환되지 않는 경우 무시
        continue
