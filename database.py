"""
Настройки базы данных на MongoDB
с указанием методов работы с БД.
"""

from model import Book

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.Library
collection = database.books


async def fetch_one_book(title):
    """
    Метод поиска книги по названию.
    """
    document = await collection.find_one({"title": title})
    return document


async def fetch_all_book():
    """
    Метод поиска списка всех книг.
    """
    books = []
    cursor = collection.find({})
    async for document in cursor:
        books.append(Book(**document))
    return books


async def create_book(book):
    """
    Метод создания книги.
    """
    document = book
    result = await collection.insert_one(document)
    return document


async def update_book(title, author, pages, date, genre, summary):
    """
    Метод обновления данных по книге.
    """
    await collection.update_one({"title": title}, {"$set": {"author": author,
                                                            "pages": pages,
                                                            "date": date,
                                                            "genre": genre,
                                                            "summary": summary}})
    document = await collection.find_one({"title": title})
    return document


async def remove_book(title):
    """
    Метод удаления книги.
    """
    await collection.delete_one({"title": title})
    return True
