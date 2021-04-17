# 3
from time import perf_counter, sleep
import csv

from bs4 import BeautifulSoup
import requests
import lxml

'''
    I took this url: https://krisha.kz/a/show/29715486
'''

URL = 'https://krisha.kz/a/show/29715486'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
    Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,\
    */*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}


def get_html(url, params=None):
    '''Here we get page's html'''
    src = requests.get(url, headers=HEADERS, params=params)
    return src


def get_content(html):
    '''Method that returns content from page'''
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div', class_='offer__advert-info')
    houses = []
    houses.append({
        'title': soup.h1
    })
    for item in items:
        #checking on the existence of price
        # проверка наличия цены
        price = item.find('div', class_ = 'offer__price')
        if price:
            price = price.get_text(strip=True)
        else:
            price = 'По запросу'
        houses.append({
            'price': price,
            'location': item.find('div', class_='offer__location offer__advert-short-info').find_next('span').get_text(strip=True),
            # 'house': item.find('div', class_='offer__advert-short-info').get_text(strip=True),
            # 'floor': item.find('div', class_='offer__advert-short-info').get_text(strip=True),
            # 'area': item.find('span', class_='offer__advert-short-info').get_text(strip=True),
            # 'condition': item.find('div', class_='offer__advert-short-info').get_text(strip=True),
            # 'complex': item.find('div', class_='offer__advert-short-info').get_next('a').get_text()
            'info': [info.text for info in item.find_all(class_='offer__advert-short-info')]

        })
    return houses


def save_in_file(items):
    '''Save file in current directory'''
    with open(r'Result.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Цена', 'Место', 'Информация'])
        for item in items:
            writer.writerow([item['price'], item['link'], item['info']])


def parse():
    '''Main method that's call everything'''
    html = get_html(URL)
    if html.status_code == 200:
        summary = []
        start = perf_counter()
        sleep(1)
        summary.extend(get_content(html.text))
        finish = perf_counter()
        save_in_file(summary)
        print(f'Парсинг закончен за {finish - start} секунд')
    else:
        print('Error')

parse()