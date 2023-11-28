# kospi.py
import requests
from bs4 import BeautifulSoup

# Crawling


# Http request method(verb)
# 1.GET  95%
# 2.POST 4%


# 요청 => 응답 객체
res = requests.get('https://finance.naver.com/sise/')
# HTML 문서 파싱 완료 결과
soup = BeautifulSoup(res.text, 'html.parser')
tag = soup.select_one('#KOSPI_now')

print(tag.text)