from datetime import datetime


def get_non_empty_input(text) -> str:
    """
    Get a non-empty input from the user.
    """
    while True:
        user_input = input(text).strip()
        if user_input:
            return user_input
        else:
            print("Пожалуйста, введите корректные данные.")


def get_year_input(text) -> int:
    """
    Get year input from the user.
    """
    while True:
        try:
            year = int(input(text))
            if year > datetime.now().year:
                print("Год не может превышать текущий. Пожалуйста, введите корректные данные.")
            else:
                return year
        except ValueError:
            print("Введите год в формате целого числа.")


def print_books(books: dict) -> None:
    """
    Print all books.
    """
    for book in books.values():
        print(f'\nID: {book["id"]}')
        print(f'Название: {book["title"]}')
        print(f'Автор: {book["author"]}')
        print(f'Год издания: {book["year"]}')
        print(f'Статус: {book["status"]}')


def check_empty_library(library: dict) -> bool:
    """
    Check if library is empty.
    """
    if len(library) == 0:
        print('Чтобы работать с книгами в библиотеке, необходимо их добавить, а у нас библиотека пуста :)')
        return True


def get_book_by_id(library: dict) -> str:
    """
    Get book by id.
    """
    while True:
        book_id = input('Введите id книги или 0 для выхода в меню: ')
        if book_id == '0':
            return '0'
        if book_id in library:
            return book_id
        else:
            print('Такой книги нет в библиотеке. Пожалуйста, введите корректные данные.')


def get_book_by_field(library: dict, search_field: str) -> dict | None:
    """
    Search book in library by field.
    """
    while True:
        match search_field:
            case 'title':
                search_value = get_non_empty_input(f'Введите название или 0 для выхода в меню: ')
            case 'author':
                search_value = get_non_empty_input(f'Введите автора или 0 для выхода в меню: ')
            case 'year':
                search_value = get_year_input(f'Введите год издания или 0 для выхода в меню: ')
        if search_value == '0':
            return
        else:
            break
    books = {}
    for book in library.values():
        if book.get(search_field) == search_value:
            books.update({book['id']: book})
    if books:
        return books
    else:
        print('Книг с таким полем в библиотеке нет')
