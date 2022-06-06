# from https://quotes.toscrape.com
# 1. get first page authors' names {set}
# 2. get first page quotes [list]
# 3. get top 10 tags for quotes
# 4. get all the authors' names
import bs4
import requests

result = requests.get('https://quotes.toscrape.com')
soup = bs4.BeautifulSoup(result.text, 'lxml')
authors_set = set()  # 1
for i in range(len(soup.select('.author'))):
    author = soup.select('.author')[i].getText()
    authors_set.add(author)
print(authors_set)

quotes = []  # 2
for i in range(len(soup.select('.text'))):
    quote = soup.select('.text')[i].getText()
    quotes.append(quote)
print([quotes])

for tag in soup.select('.tag-item'):
    print(tag.text)  # 3

all_authors = set()  # 4
page = 1
while True:
    url = f'https://quotes.toscrape.com/page/{page}'
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    if 'No quotes found!' in result.text:
        break
    for i in range(len(soup.select('.author'))):
        author = soup.select('.author')[i].getText()
        all_authors.add(author)
    page += 1
print(all_authors)
