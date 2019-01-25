import requests

url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo="

for i in range(837, 842):
    url = f"https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={i}"
    response = requests.get(url).json()
    print(response['drwtNo1'])
