import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get("https://daum.net")

elem = browser.find_element(By.ID, 'q')
elem.send_keys("다음 주식")
elem.send_keys(Keys.ENTER)
elem = browser.find_element(By.CLASS_NAME, 'f_url')
elem.click()

browser.get("https://naver.com")
browser.switch_to.window(browser.window_handles[0])
time.sleep(3)
elem = browser.find_element(By.CLASS_NAME, 'service_icon type_stock')
elem.click()



# html위치 찾기 - requests:select
# elem = browser.find_element(By.CLASS_NAME,'MyView-module__link_login___HpHMW')
# elem.click()
# elem = browser.find_element(By.NAME,'pw')
# elem.click()
# browser.back()
# browser.forward()
# browser.refresh()

# elem = browser.find_element(By.ID,'query')

# elem.send_keys("네이버 영화") # 글자 입력
# elem.send_keys(Keys.ENTER) # 엔터키 입력

# browser.switch_to.window(browser.window_handles[1])



time.sleep(100)