from bs4 import BeautifulSoup
import requests


basic_url = 'https://books.toscrape.com/catalogue/page-{}.html'


for i in range(50):
    print('https://books.toscrape.com/catalogue/page-{}.html'.format(i))