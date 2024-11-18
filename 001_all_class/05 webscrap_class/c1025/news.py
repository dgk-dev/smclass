import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from bs4 import BeautifulSoup
import requests

# SMTP 서버 정보 설정
smtp_name = "smtp.naver.com"
smtp_port = 587

# 자신의 네이버 메일 주소, 비밀번호, 수신자 이메일 주소
send_email = "solicitor_@naver.com"
pw = ""  # 보안을 위해 실제 코드에서는 환경 변수를 사용하세요
recv_email = "kangmumu@gmail.com"

# 이메일 제목과 내용 설정
title = "제목 : 파이썬 이메일보내기 안내"
content = "파일을 첨부합니다"

# MIME 멀티파트 메시지 생성
msg = MIMEMultipart()
msg["Subject"] = title
msg["From"] = send_email
msg["To"] = recv_email
msg.attach(MIMEText(content))

# 웹사이트에서 언론 이름과 기사 제목 5개 추출
url = "https://news.naver.com/main/ranking/popularDay.naver"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.select('#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking > div')
    news_data = []
    
    for article in articles:
        media_name = article.select('a > strong')
        title = article.select('a')
        news_data.append(f"{media_name} - {title}")
    
    # 파일 저장
    with open("news_articles.txt", "w", encoding="utf-8") as f:
        for line in news_data:
            f.write(line + "\n")
    
    # 파일 첨부
    with open("news_articles.txt", "rb") as f:
        attachment = MIMEApplication(f.read())
        attachment.add_header('Content-Disposition', 'attachment', filename='news_articles.txt')
        msg.attach(attachment)
else:
    print("Error: 뉴스 웹페이지를 불러오지 못했습니다.")
    exit()

# SMTP 서버 연결 및 이메일 전송
try:
    s = smtplib.SMTP(smtp_name, smtp_port)
    s.starttls()  # TLS 보안 연결 시작
    s.login(send_email, pw)
    s.sendmail(send_email, recv_email, msg.as_string())
    print("메일이 발송되었습니다.")
except Exception as e:
    print(f"Error: 이메일 발송 중 문제가 발생했습니다: {e}")
finally:
    s.quit()
