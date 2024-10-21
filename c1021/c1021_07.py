import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
newList = soup.find("div",{"class":"rankingnews_box_wrap"}).find("div",{"class":"rankingnews_box"})
titles = newList.find("ul",{"class":"rankingnews_list"}).find_all("a",{"class":"list_title nclicks('RBP.rnknws')"})

with open("a.txt","w",encoding="utf-8") as f:
    f.write(newList.find("strong",{"class":"rankingnews_name"}).text)
    f.write("\n")
    for i, title in enumerate(titles):
        f.write(f"{i+1}. {title.get_text()}\n")
