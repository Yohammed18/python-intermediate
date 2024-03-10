import bs4, lxml, requests

# store the url where the scraping will be done
url = 'https://www.videoschool.com/'

# get the request
response = requests.get(url)

# Chek that the status code is 200
# print(response)

# utilize BeautifulSoup to conduct scrapping
soup = bs4.BeautifulSoup(response.text, 'html.parser')

# get the the 6 th paragraph text
paragraph_6 = soup.select('p')[6].getText()

# print the paragraph on the
# print(paragraph_6)
central_block = soup.select('.content-container')

for h in central_block:
    print(h.getText()+'\n')