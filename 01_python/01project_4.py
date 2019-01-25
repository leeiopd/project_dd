import requests
import os
import urllib.request
import csv
import pprint
import shutil


with open('movie_naver.csv', 'r', encoding='utf-8', newline='') as f:
    movie_naver = csv.DictReader(f)
    for m_info in movie_naver:
        m_code = m_info['movie_code']
        file_url = m_info['thumb_url']
        file_name = f'{m_code}.jpg'

        if file_url:
            try:
                with open(f'./images/{file_name}', 'wb') as f:
                    img = requests.get(file_url).content
                    f.write(img)
            except FileNotFoundError:
                os.mkdir('./images/')

        
