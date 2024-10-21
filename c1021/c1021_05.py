import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml") # str -> html태그,css태그 사용될수 있는

# print(soup.title) # 제일먼저 찾아지는 것을 출력
# print(soup.find("title")) # 특정 위치의 태그와 속성을 가지고 찾을 수 있다.
soup.find("div",{"class":"rankingnews_box_wrap"})
newLists = soup.find_all("div",{"class":"rankingnews_box"})
print(len(newLists))

for newList in newLists:
    print(newList.find("strong",{"class":"rankingnews_name"}).text)






# rankingnews_wrap = soup.find("div",{"class":"rankingnews_box_wrap"})

# rankingnews_boxs = rankingnews_wrap.find("div",{"class":"rankingnews_box"})
# print(rankingnews_boxs.find("strong",{"class":"rankingnews_name"}).text)


