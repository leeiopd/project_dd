import requests
import os
import pprint
import csv



key = os.getenv('kobis_key')
url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd="


m_info_list = []
with open('boxoffice.csv', 'r', encoding='utf-8', newline='') as f:
    boxoffice = csv.DictReader(f)
    for movie_info in boxoffice:
        url_m = url + movie_info['movie_code']
        response_movie = requests.get(url_m).json()

        lists_m = response_movie['movieInfoResult']['movieInfo']
        
        movie_code = movie_info['movie_code']
        movie_name_ko = movie_info['title']
        movie_name_en = lists_m['movieNmEn']
        movie_name_og = lists_m['movieNmOg']
        prdt_year = lists_m['openDt']
        show_Time = lists_m['showTm']
        directors = lists_m['directors'][0]['peopleNm']
        show_Time = lists_m['showTm']
        
        try:
            genres = lists_m['genres'][0]['genreNm']
        except IndexError:
            genres = ''

        try:
            watch_Grade = lists_m['audits'][0]['watchGradeNm']
        except IndexError:
            watch_Grade = ''

        try:
            actors1 = lists_m['actors'][0]['peopleNm']
        except IndexError:
            actors1 = ''
        try:
            actors2 = lists_m['actors'][1]['peopleNm']
        except IndexError:
            actors2 = ''
        try:
            actors3 = lists_m['actors'][2]['peopleNm']
        except IndexError:
            actors3 = ''

        
        m_info = {'movie_code':movie_code, 'movie_name_ko':movie_name_ko, 'movie_name_en':movie_name_en, 'movie_name_og':movie_name_og,
                'prdt_year':prdt_year, 'show_Time':show_Time, 'genres':genres,
                'directors':directors, 'watch_Grade':watch_Grade,'actors1':actors1, 'actors2':actors2, 'actors3':actors3}
        m_info_list.append(m_info)


with open('movie.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movie_code', 'movie_name_ko', 'movie_name_en', 'movie_name_og', 'prdt_year', 'show_Time', 'genres', 'directors', 'watch_Grade', 'actors1', 'actors2', 'actors3' ]
    write = csv.DictWriter(f, fieldnames=fieldnames)
    write.writeheader()

    for movie in m_info_list:
        write.writerow(movie)
