class Book():
    pass

def make_book(name, author, genre, year,pages):
    book = Book()
    book.name = name #book.__dict__['name'] = name
    book.autor = author #book.__dict__['author'] = author
    book.genre = genre #book.__dict__['genre'] = genre
    book.year = year #book.__dict__['year'] = year
    book.pages = pages #book.__dict__['pages'] = pages
    return book

flash_forward = make_book('Flash Forward', 'Someone', 'Sci-fi', 1990, 2000)
spiderman = make_book('Spiderman', 'Stan Lee', 'Action Comics', 1964, 100)
rp1 = make_book('Ready Player 1', 'SomeGuy', 'Sci-fi', 2010, 150)
lib = [flash_forward, spiderman, rp1]
i = input('Enter the name of the book: ')
libdict = {Book.name: Book for Book in lib}
print(libdict[i.title()].__dict__)