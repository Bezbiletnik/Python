import csv
import time 

from bs4 import BeautifulSoup
import requests
import lxml


URL = ''
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

DATA = {
    
}

session = requests.Session()

html = session.post(URL, headers=HEADERS, data=DATA).text

# with open('Parsers/Result.html', 'w') as file:
#     file.write(html)

# with open('Parsers/Result.html') as file:
#     html = file.read()

soup = BeautifulSoup(html, 'lxml')
items = soup.find_all('div', class_='audio_row__inner')

music = []
for item in items:
    music.append({
        'title': item.find_all('span', class_='audio_row__title_inner _audio_row__title_inner').get_text(strip=True),
        'author': item.find_all('a').get_text(strip=True),
        'link': item.find_all('a').get('href'),
        'durability': item.find_all('div', class_='audio_row__info _audio_row__info').find_next('div', class_='audio_row__duration audio_row__duration-s _audio_row__duration').get_text(strip=True)
        })
print(music)

def save_file(items):
    with open('Parsers/Music.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Название", "Автор", "Ссылка(Автор)", "Длительность"])
        for item in items:
            writer.writerow([item['title'], item['author'], item['link'], item['durability']])

save_file(music)