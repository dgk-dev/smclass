from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import pyautogui

url = "https://www.yanolja.com/search/%EA%B0%95%EB%A6%89%20%ED%98%B8%ED%85%94?pageKey=1729747969396"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

pyautogui.moveTo(960, 540)
time.sleep(2)
pyautogui.moveTo(50, 100)
time.sleep(2)
pyautogui.moveTo(960,540)
time.sleep(2)
browser.
pyautogui.moveTo(960,540)


