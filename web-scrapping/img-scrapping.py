from bs4 import BeautifulSoup
import requests, lxml

# PARSING - parsing refers to the process of analyzing a piece of text or data according to a specific set of rules or syntax
url = 'https://www.videoschool.com/'

respone = requests.get(url)
# print(respone)

# lmlx and html.parser are python libraries used to parse HTML and XML documents
soup = BeautifulSoup(respone.text, 'lxml')

images = soup.select('.img-responsive')[0]['src']

# for image in images:
#     print(image)

print(images)

image1 = requests.get(images)
# wb stand for write binary
f = open('my_image.jpg', 'wb')
f.write(image1.content)
f.close()