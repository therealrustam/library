# Проект Library

## Описание

Library - это API сервис для учета книг в домашней библиотеке. Есть возможность добавлять/удалять/редактировать данные о книге, а также получение данных об одной книге или о всех книгах в библиотеке.
Сервис создан на основе фреймворка FastAPI языка программирования Python. В качестве базы данных был использована документоориентированная система управления базами данных MongoDB.

## Установка

Клонируйте новый репозиторий себе на компьютер.
Разверните в репозитории виртуальное окружение: в папке скачанного репозитория выполните команду: python -m venv venv
Активируйте виртуальное окружение.
В виртуальном окружении установите зависимости: pip install -r requirements.txt

## Стек технологии

- anyio==3.5.0
- asgiref==3.5.1
- autopep8==1.6.0
- click==8.1.3
- colorama==0.4.4
- fastapi==0.76.0
- h11==0.13.0
- idna==3.3
- importlib-metadata==4.11.3
- motor==3.0.0
- pycodestyle==2.8.0
- pydantic==1.9.0
- pymongo==4.1.1
- sniffio==1.2.0
- starlette==0.18.0
- toml==0.10.2
- typing_extensions==4.2.0
- uvicorn==0.17.6
- zipp==3.8.0


## Примеры

Примеры запросов по API:

- [GET] /api/v1/posts/ - Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией.
- [POST] /api/v1/posts/ - Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.
- [GET] /api/v1/posts/{id}/ - Получение публикации по id.
- [PUT] /api/v1/posts/{id}/ - Обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены.
- [PATCH] /api/v1/posts/{id}/ - Частичное обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены.
- [DELETE] /api/v1/posts/{id}/ - Удаление публикации по id. Удалить публикацию может только автор публикации. Анонимные запросы запрещены.


## Авторы

Вахитов Рустам
