"""
Настройки API приложения Library.
"""

from fastapi import FastAPI, HTTPException

from model import Book
from database import (
    fetch_one_book,
    fetch_all_book,
    remove_book,
    create_book,
    update_book
)

app = FastAPI(title="Library")

origins = ['https://localhost:3000']


@app.get('/books/')
async def get_books():
    """
    Метод получения списка
    всех книг в библиотеке.
    """
    response = await fetch_all_book()
    return response


@app.get('/books/{title}')
async def get_book(title):
    """
    Метод получения книги
    по названию.
    """
    response = await fetch_one_book(title)
    if response:
        return response
    raise HTTPException(404, f'There is no Book item with this title {title}')


@app.post('/books/', response_model=Book)
async def post_book(book: Book):
    """
    Метод создания книги.
    """
    response = await create_book(book.dict())
    if response:
        return response
    raise HTTPException(400, 'Something went wrong / Bad Request')


@app.put('/books/{title}', response_model=Book)
async def put_book(title: str, author: str, pages: int, date: str, genre: str, summary: str):
    """
    Метод редактирования данных книги.
    """
    response = await update_book(title, author, pages, date, genre, summary)
    if response:
        return response
    raise HTTPException(404, f'There is no Book item with this title {title}')


@app.delete('/books/{title}')
async def delete_book(title):
    """
    Метод удаления книги.
    """
    response = await remove_book(title)
    if response:
        return 'Succesfully deleted book item!'
    raise HTTPException(404, f'There is no Book item with this title {title}')
