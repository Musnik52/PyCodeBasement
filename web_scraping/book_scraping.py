# from books.toscrape.com, show me the names of all the books rated 2 stars.

import bs4
import requests

two_star_titles = []
for page in range(1, 51):
    result = requests.get(
        f'https://books.toscrape.com/catalogue/page-{page}.html')
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    books = soup.select('.product_pod')
    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            i = book.select('a')[1]['title']
            two_star_titles.append(i)
for title in two_star_titles: 
    print(title)
    print()
