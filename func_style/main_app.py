import time
from book_management import add_book, delete_book, search_books, get_all_books, change_book_status
from book_storage import save_library, load_library


def main_menu() -> None:
    """
    Функция вывода основного меню.
    """
    library = load_library()
    while True:
        print('\nОсновное меню. Выберите действие:')
        print('1. Добавить книгу')
        print('2. Удалить книгу')
        print('3. Поиск книги')
        print('4. Показать все книги')
        print('5. Изменить статус книги')
        print('6. Выход')
        user_choice = input('Введите номер действия: ')
        time.sleep(1)
        match user_choice:
            case '1':
                print('1. Добавить книгу')
                add_book(library)
                save_library(library)
            case '2':
                print('2. Удалить книгу')
                delete_book(library)
                save_library(library)
            case '3':
                print('3. Поиск книги')
                search_books(library)
            case '4':
                print('4. Показать все книги')
                get_all_books(library)
            case '5':
                print('5. Изменить статус книги')
                change_book_status(library)
                save_library(library)
            case '6':
                save_library(library)
                print('Данные успешно сохранены. До свидания!')
                time.sleep(1)
                break
            case _:
                print('Введите корректный номер действия')


if __name__ == '__main__':
    print('Добро пожаловать!')
    main_menu()
