# 웹스크래핑 세팅
import requests
# res = requests.get("https://www.google.com/")
res = requests.get("https://www.naver.com/")
# res = requests.get("https://www.melon.com/index.htm")
res.raise_for_status()

# requests 정보를 가져올시
# 제이쿼리, 자바스크립트,외부페이지,react,vue.. 비동기식으로 작동되는 소스는 
# 가져오지 못함.

print("총 문자 길이 :",len(res.text))

# f.close()를 적을 필요가 없음. 더 권장됨
with open("b.html","w",encoding="utf-8") as f:
    f.write(res.text)

# print(res.text) # html 소스 출력

# # 파일 저장
# f = open("a.html","w",encoding="utf-8")
# f.write(res.text)
# f.close()


# if res.status_code == 200:
#     print(res.text)
# else:
#     print("접근할 수 없습니다.")
# print("응답코드 : ", res.status_code)

# print(res.text)