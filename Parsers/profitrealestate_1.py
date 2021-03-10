'''Parser for "profit real estate" site'''
from time import perf_counter, sleep
import csv

from bs4 import BeautifulSoup
import requests
import lxml

URL = 'https://profitrealestate.ru/catalog/sell/Alaniia?content_id=&price_from=&price_to=&order=1'
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
    items = soup.find_all('div', class_='catalog-change__object-item')
    houses = []
    for item in items:
        #checking on the existence of price
        # проверка наличия цены
        price = item.find('span', class_ = 'price').find_next('span')
        if price:
            price = price.get_text()
        else:
            price = 'По запросу'
        houses.append({
            #'price': item.find('span', class_='object-price').get_text(strip=True),
            'price': price,
            #Under, comment finds all links, that are in page.
            #'link': item.find('a').get('href'),
            #This line, below the comment, finds the link more directionally
            'link': item.find('div', class_='catalog-change__object-item-photo-block').find_next('a').get('href'),
            'location': item.find('div', class_='main-block5__object-information-location').get_text(strip=True),
            'rooms': item.find('div', class_='main-block5__object-information-appartment').get_text(strip=True),
            'area': item.find('span', class_='hot-deals__descript-span').get_text(strip=True),
            'year': item.find('div', class_='main-block5__object-information-year').get_text(strip=True)

        })
    return houses

def get_pages_count(html):
    '''Pages counting'''
    soup = BeautifulSoup(html, 'lxml')
    pagination = soup.find_all('a', class_='number')
    if pagination:
        return int(pagination[-1].get_text(strip=True))
    else:
        return 1

def save_in_file(items):
    '''Save file in current directory'''
    with open('Parsers/Result.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Цена', 'Ссылка',\
                        'Место', 'Кол-во комнат',\
                        'Площадь', 'Год строительства'])
        for item in items:
            writer.writerow([item['price'], item['link'],\
                             item['location'], item['rooms'],\
                             item['area'], item['year']])

def parse():
    '''Main method that's call everything'''
    html = get_html(URL)
    if html.status_code == 200:
        summary = []
        start = perf_counter()
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            sleep(1)
            print(f'Происходит парсинг страницы {page} из {pages_count}')
            html = get_html(URL, params={'page': page})
            summary.extend(get_content(html.text))
        #print(summary)
        finish = perf_counter()
        save_in_file(summary)
        print(f'Парсинг закончен за {finish - start} секунд')
    else:
        print('Error')

parse()
