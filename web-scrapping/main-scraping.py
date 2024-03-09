# in order to conduct web scrapping you'll need to install 3 modules
# beautifulsoup4, lxml, and requests
import requests, lxml
from bs4 import BeautifulSoup
# we will web scrape the site https://www.videoschool.com/

# Let's capture the title
url = 'https://www.videoschool.com/'
response = requests.get(url)
# print out the response to see the content
# print(response.text)

# B Soup will allow us to scan throuh the html file 
soup = BeautifulSoup(response.text, 'html.parser')

# This will return a list of element in that tag
# print(len(soup.select('h1')))
# print(soup.select('title')[0].getText())
my_p = soup.select('h1')[1].getText()
print(my_p)

# parse html file via soup
