from bs4 import BeautifulSoup
import requests, os
from urllib.parse import urljoin

# Create the img directory if it doesn't exist
# Get the absolute path of the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(script_dir, 'img')

basic_url = 'https://books.toscrape.com/catalogue/page-{}.html'

high_rated_titles = []


for i in range(1, 5):
    # asign the url that will be scrapped
    url = 'https://books.toscrape.com/catalogue/page-{}.html'.format(i)

    # send a request to get the HTTP 200 code response
    response = requests.get(url)
    print(response)

    # use soap to get the file content to parse
    soap = BeautifulSoup(response.text, 'html.parser')

    books = soap.select('.product_pod ')

    # let's check how many books and store each start
    for book in books:
        # check if the book is of rating 5 stars
        if book.select('.star-rating.Five'):
            # retrieve the title of the book
            book_title = book.select('h3')[0].getText()
            # print the book title 
            print(book_title)
            high_rated_titles.append(book_title)
            # retrieve the picture of the book src 
            img_src = book.select('.thumbnail')[0]['src']
            img_url = urljoin(url, img_src)
            # img_src = 'https://books.toscrape.com/'+img_src[2:]
            # print(img_src)
            # make a request to retrieve the image that you will save
            image = requests.get(img_url)

            # download the picture to the 5-starts-img
            file_name = os.path.join(img_dir, '{}.jpg'.format(book_title))
            file = open(file_name, 'wb')
            file.write(image.content)
            file.close()
    


# web-scrapping\scrapping-project\img

