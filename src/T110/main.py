from lib.lib import Lib
from lib.book import Book

lib = Lib()
loop = True
while loop:
    print('Добро пожаловать в редактор библиотеки. Выберите действие:')
    print('1 - Создать книгу')
    print('2 - Удалить книгу')
    print('3 - Изменить название книги')
    print('4 - редактировать книгу')
    print('5 - Вывести всю информацию о имеющихся книгах')
    print('любая другая главиша выход')
    choice = input('Ваш выбор:  ')
    if choice == '1':
        name_book = input('Введите название книги которую хотите создать: ')
        lib.add_book(name_book)
    elif choice == '2':
        name_book = input('Введите название книги которую хотите удалить: ')
        lib.delete_book(name_book)
    elif choice == '3':
        old_book = input('Введите название книги которое хотите поменять: ')
        new_book = input('Введите новое название: ')
        lib.chenge_name(old_book, new_book)
    elif choice == '4':
        loop2 = True
        while loop2:
            choice_book = input('Введите название книги которую хотите редактировать: ')
            book = Book(choice_book)
            check_book = book.choose_book()
            if check_book:
                print('1 - Добавить главу в книгу')
                print('2 - Изменить название главы')
                print('3 - Удалить главу')
                print('любая другая главиша выход в главное меню')
                choice_used_chapter = input('Выберите действие: ')
                if choice_used_chapter == '1':
                    name_chapter = input('Введите название главы которую хотите создать: ') + '.txt'
                    book.add_chapter(name_chapter)
                elif choice_used_chapter == '2':
                    old_name_chapter = input('Введите название главы которое хотите поменять: ') + '.txt'
                    new_name_chapter = input('Введите новое название: ') + '.txt'
                    book.chenge_chapter(old_name_chapter, new_name_chapter)
                elif choice_used_chapter == '3':
                    name_chapter = input('Введите название главу которую хотите удалить: ') + '.txt'
                    book.delete_chapter(name_chapter)
            else:
                loop2 = False
    elif choice == '5':
        lib.full_info()
    else:
        loop = False
