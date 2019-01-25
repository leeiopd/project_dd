import requests
import os
import pprint
import csv


# 대표코드, 영화명, 해당일 누적관객수(최신), 해당일
# movieCd, movieNm, audiAcc, date

key = os.getenv('kobis_key')

datelist = ['20181111', '20181118', '20181125', '20181202', '20181209',
            '20181216', '20181223', '20181230', '20190106', '20190113']

datelist.sort(reverse=True)

url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt="
weekset = "&weekGb=0&multiMovieYn&repNationCd&wideAreaCd"

info_list = {}


cnt = 0
for date in datelist:
    geturl = url + date + weekset
    response = requests.get(geturl).json()
    lists = response['boxOfficeResult']['weeklyBoxOfficeList']

    for movie in lists:
        movieCd = movie['movieCd']
        movieNm = movie['movieNm']
        audiAcc = movie['audiAcc']
        info_list[movieCd]={'recorded_at': date, 'title': movieNm,
                'movie_code': movieCd, 'audience': audiAcc}


boxoffice=[]
for i in info_list.values():
    boxoffice.append(i)

with open('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movie_code', 'title', 'audience', 'recorded_at']
    write = csv.DictWriter(f, fieldnames=fieldnames)
    write.writeheader()

    for movie in boxoffice:
        write.writerow(movie)