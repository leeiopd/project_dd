import csv
lunch = {
    '맘스터치' : '싸이버거',
    '노은각' : '짬짜면',
    '신전떡볶이' : '김밥'
}

# file - with로 파일 만들기
with open('lunch.csv', 'w', encoding='utf-8') as f:
    for key, value in lunch.items():
        f.write(f'{key}, {value}\n')



lunch2 = [
    {
        'store' : '맘스터치',
        'menu' : '싸이버거'
    },
    {
        'store' : '노은각',
        'menu' : '짬짜면'
    }
]

with open('lunch2.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['store', 'menu']
    write = csv.DictWriter(f, fieldnames=fieldnames)
    write.writeheader()
    #write.writerow({'menu':'짬짜면', 'store':'노은각'})
    
    for l in lunch2:
        write.writerow(l)

lunch3 = {
    '맘스터치':'싸이버거',
    '노은각':'짬짜면'
}
with open('lunch3.csv', 'w', encoding='utf-8', newline='') as f:
    write = csv.writer(f)
    write.writerow(('가게', '메뉴'))
    for item in lunch3.items():
        # item은 ( key, value ) 의 tuple형이 호출된다.
        write.writerow(item)


with open('lunch3.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['가게'], row['메뉴'])