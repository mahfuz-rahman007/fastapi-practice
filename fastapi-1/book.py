from fastapi import Body,FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Book 1", "author": "Rogers", "category": "Programming"},
    {"title": "Book 2", "author": "Steve", "category": "Science"},
    {"title": "Book 3", "author": 'Steve', "category": "Math"},
    {"title": "Book 4", "author": "Mark", "category": "Math"}
]

@app.get('/')
async def start():
    return {
        "message": "Hello Mahfuz! Welcome to Fast APi"
    }

@app.get('/books')
async def start():
    return BOOKS

@app.get('/book/{title}')
async def get_single_book(title: str):
    for book in BOOKS:
        if book.get('title').casefold() == title.casefold():
            return book
    return 'Not Found'

@app.get('/book/{author}/')
async def get_book_by_author(author:str, category:str = None):
    book_list = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold() and book.get('category').casefold() == category.casefold():
            book_list.append(book)
    
    return book_list if len(book_list) > 0 else 'Not Found'

@app.post('/book/create-book')
async def create_new_book(new_book=Body()):
    BOOKS.append(new_book)

@app.put('/book/update-book')
async def update_book(new_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == new_book.get('title').casefold():
            BOOKS[i] = new_book
    return "Update Success"
