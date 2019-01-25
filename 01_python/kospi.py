import requests # 소스 코드 내용을 받아오는 라이브러리
from bs4 import BeautifulSoup


# 1. 요청 보낼 url을 저장한다.
url = "https://finance.naver.com/sise/"

# 2. 해당 url로 요청을 보내서 내용을 저장한다.
response = requests.get(url).text
# requests.get(url).json()

# 3. 받은 html파일을 파이썬으로 찾기 편하도록 bs4를 사용한다,
html = BeautifulSoup(response, 'html.parser')
print(html)
# 4. 선택자를 이용해서 값을 골라낸다.(코스피 지수)
kospi = html.select_one('#KOSPI_now') # ID선택자는 '#'
print(kospi.text)