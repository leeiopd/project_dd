import requests
import os
import pprint
import csv


client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }

url = f'https://openapi.naver.com/v1/search/movie.json?query='
movie_naver = []
with open('movie.csv', 'r', encoding='utf-8', newline='') as f:
    movies = csv.DictReader(f)
    for m_info in movies:
        movie_name_ko = m_info['movie_name_ko']
        movie_code = m_info['movie_code']

        search_url_naver = f'https://openapi.naver.com/v1/search/movie.json?query={movie_name_ko}'
        response_naver = requests.get(search_url_naver, headers=headers).json()
        pprint.pprint(response_naver)
            
        try:
            thumb_url = response_naver['items'][0]['image']
        except (IndexError, KeyError):
            thumb_url = ''
        try:           
            link_url = response_naver['items'][0]['link']
        except (IndexError, KeyError):
            link_url = ''
        try:
            user_rating = response_naver['items'][0]['userRating']
        except (IndexError, KeyError):
            user_rating = ''

        naver_info = {'movie_name_ko':movie_name_ko, 'movie_code':movie_code, 'thumb_url':thumb_url, 'link_url':link_url, 'user_rating':user_rating}
        movie_naver.append(naver_info)

with open('movie_naver.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movie_name_ko', 'movie_code', 'thumb_url', 'link_url', 'user_rating']
    write = csv.DictWriter(f, fieldnames=fieldnames)
    write.writeheader()

    for data in movie_naver:
        write.writerow(data)