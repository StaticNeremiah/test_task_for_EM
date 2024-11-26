from uuid import uuid4
import time
from utils import (get_non_empty_input, get_year_input, check_empty_library,
                   print_books, get_book_by_id, get_book_by_field)


def add_book(library: dict) -> dict:
    """
    Add book to library.
    """
    while True:
        title = get_non_empty_input('Введите название книги: ')
        author = get_non_empty_input('Введите автора книги: ')
        year = get_year_input('Введите год издания книги: ')
        book_id = str(uuid4())
        book: dict = {
            'id': book_id,
            'title': title,
            'author': author,
            'year': year,
            'status': 'В наличии'
        }
        library[book_id] = book
        print(f'\nКнига с названием: {title} добавлена в библиотеку.\nID: {book_id}\n')
        time.sleep(1)
        if input('Добавить еще книгу? (д/н) ') == 'д':
            continue
        else:
            time.sleep(1)
            print('\nВозвращение в  основное меню')
            return library


def delete_book(library: dict) -> dict:
    """
    Delete book from library.
    """
    while True:
        if check_empty_library(library):
            return {}
        book_id = get_book_by_id(library)
        if book_id == '0':
            break
        try:
            library.pop(book_id)
            print(f'\nКнига с id: {book_id} удалена.')
            time.sleep(1)
            print('Возвращение в  основное меню')
            return library
        except KeyError:
            print('Книги с таким id нет в библиотеке')
            continue


def search_books(library: dict) -> None:
    """
    Search books by title, author, year.
    """
    while True:
        if check_empty_library(library):
            return
        print('По какому полю вы хотите найти книгу?')
        while True:
            search_field = input('1. Название, 2. Автор, 3. Год издания, 0. Выход: ')
            match search_field:
                case '1':
                    search_field = 'title'
                case '2':
                    search_field = 'author'
                case '3':
                    search_field = 'year'
                case '0':
                    return
                case _:
                    print('Введите корректный номер поля')
                    continue
            if search_field in ('title', 'author', 'year'):
                break
        books = get_book_by_field(library, search_field)
        if books is None:
            break
        print_books(books)
        break


def get_all_books(library: dict) -> None:
    """
    Print all books in library.
    """
    if check_empty_library(library):
        return
    else:
        print('Книги в библиотеке:')
        print_books(library)


def change_book_status(library: dict) -> dict:
    """
    Change book status.
    """
    while True:
        if check_empty_library(library):
            return {}
        book_id = get_book_by_id(library)
        if book_id == '0':
            break
        print(f'Статус книги с id: {book_id} - {library[book_id]["status"]}')
        while True:
            status = input('Выберите новый статус книги: 1. В наличии, 2. Выдана, 0. Выход в меню ')
            match status:
                case '1':
                    status = 'В наличии'
                case '2':
                    status = 'Выдана'
                case '0':
                    return
                case _:
                    print('Введите корректный номер статуса')
                    continue
            library[book_id]['status'] = status
            print(f'Статус книги с id: {book_id} изменен на {status}')
            break
        return library
