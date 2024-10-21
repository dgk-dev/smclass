import requests
from bs4 import BeautifulSoup

url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
itemwrap = soup.find("div",{"id":"bestPrdList"}).find("div",{"class":"viewtype"}).find("ul",{"class":"cfix"})
items = itemwrap.find_all("li")
print(len(items))

for i, item in enumerate(items):
    print(f"{i+1}. {item.find("div",{"class":"pname"}).find("p").text}\t")
    print(f"{item.find("strong",{"class":"sale_price"}).text}원\n")


