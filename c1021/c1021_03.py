# naver 파일저장. 리솜리조트 파일저장

import requests

# url = [
#     "https://naver.com",
#     "https://www.resom.co.kr/resom/main/main.asp",
#     "https://www.daum.net/"
# ]

url = ["http://www.coupang.com"]

headers =  {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}

for i in range(len(url)):
    res = requests.get(url[i], headers=headers)
    res.raise_for_status()
    
    with open(f"{i}.html", "w", encoding="utf-8") as f:
        f.write(res.text)


print("프로그램을 종료합니다.")