"""
Описание моделей.
"""

from pydantic import BaseModel


class Book(BaseModel):
    """
    Модель книги.
    """
    title: str
    author: str
    pages: int
    date: int
    genre: str
    summary: str
