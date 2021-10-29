from bs4 import BeautifulSoup
import requests

URL = 'http://fapl.ru/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

req = requests.get(URL, headers= HEADERS)
src = req.text
#print(src)

with open('Parsers/index.html', 'w', encoding='') as file:
    file.write(src)