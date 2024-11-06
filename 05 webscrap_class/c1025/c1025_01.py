from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random
import csv

# # 네이버 쇼핑 검색창 입력 enter키 입력
# # 네이버 쇼핑 클릭
# # 네이버 쇼핑에서 무선 마우스 검색창 입력 enter키 입력

# url = "https://www.naver.com/"
# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)

# # 네이버 홈에서 쇼핑 아이콘 클릭
# browser.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[4]/a').click()
# time.sleep(1)

# # 현재 모든 윈도우 핸들을 가져옵니다.
# all_tabs = browser.window_handles

# # 첫 번째 탭 (기존 탭)은 `all_tabs[0]`이고, 새로 열린 탭은 `all_tabs[1]`입니다.
# browser.switch_to.window(all_tabs[1])  # 새로 열린 탭으로 전환

# browser.find_element(By.XPATH,'//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input').send_keys('무선 마우스')
# browser.find_element(By.XPATH,'//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input').send_keys(Keys.ENTER)
# time.sleep(1)

# prev_height = browser.execute_script("return document.body.scrollHeight")
# page = 1

# while page < 5:
#   browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#   time.sleep(1)
#   # 페이지가 로딩되면서 길어진 길이를 다시 가져옴.
#   curr_height = browser.execute_script("return document.body.scrollHeight")
#   # 페이지를 스크롤해서 길이가 더 길어졌는지 확인
#   if prev_height == curr_height:
#     soup = BeautifulSoup(browser.page_source,"lxml")
#     # html저장하기
#     with open(f'smclass/c1025/navershopping{page}.html','w',encoding='utf-8') as f:
#         f.write(soup.prettify())
#     page += 1
#     browser.find_element(By.CSS_SELECTOR,f'#content > div.style_content__xWg5l > div.pagination_pagination__fsf34 > div > a:nth-child({page})').click()
#   # 더 길이가 길어졌으면, 이전길이에 현재길이를 입력시킴
#   prev_height = curr_height

# print("스크래핑 완료")  
# input("Enter키를 입력하면 스크래핑이 완료되고, 데이터 분석이 시작됩니다.")

product_list = []



for page_num in range(1, 6):  # 페이지 번호 1부터 5까지 반복
    file_name = f'smclass/c1025/navershopping{page_num}.html'  # 같은 폴더에 있는 HTML 파일 이름
    with open(file_name, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')
    
    list = soup.select('div.product_item__MDtDF')

    for product in list:
        name = product.select_one("div.product_title__Mmw2K a")
        price = product.select_one("span.price_num__S2p_v > em")
        rate = product.select_one("a > span.product_grade__IzyU3")
        if rate != None:
            rate = rate.text.replace("\n","").replace("별점","").replace(" ","")
        else:
            rate = 0
        product_list.append({
            'name':name.text.strip().replace("\n",""),
            'price':int(price.text.strip().replace(",","").replace("\n","")),
            'rate':float(rate)
            })
        
# 평점 순으로 정렬 (높은 평점 순으로)
sorted_product_list = sorted(product_list, key=lambda x: x['rate'], reverse=True)

# 평점 기준
rate_filter = 4.95
print(f"평점 {rate_filter} 이상의 제품만 출력합니다.")
print("-"*60)

# 정렬된 결과 출력
for product in sorted_product_list:
    if product['rate'] >= rate_filter:
        print(f"상품명: {product['name']}, 가격: {product['price']}원, 평점: {product['rate']}")

with open(file_name, 'w', encoding='utf-8') as file:
    

