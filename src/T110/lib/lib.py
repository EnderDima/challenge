import os
import shutil
from pathlib import Path


class Lib:
    def __init__(self):
        with open(Path(__file__).parent / 'id', 'r', encoding='utf-8') as id:
            self.id = id.read()
        self.elektron_lib_path = Path(__file__).parent.parent / 'elektron_lib'
        self.elektron_lib_path.mkdir(exist_ok=True)
        base_dir = Path(__file__).parent.parent
        elektron_lib_path = base_dir / 'elektron_lib'
        elektron_lib_path.mkdir(exist_ok=True)
        self.book_path = elektron_lib_path

    def add_book(self, name_book):  # функция добавления новой книги
        book_path = self.book_path / name_book
        try:
            book_path.mkdir(exist_ok=False)  # проверка на существование одинаковых по названию книг
            book_path = self.book_path / name_book / 'info.txt'  # Создание файла с информацией
            with open(book_path, 'w', encoding='utf-8') as info:
                # Запись данных в файл с информацией
                info.write('Индекс: ' + str(self.id) + '\n Название книги: ' + name_book + '\n глав 0')
            with open(Path(__file__).parent / 'id', 'w', encoding='utf-8') as id:
                self.id = str(int(self.id) + 1)
                id.write(self.id)
        except FileExistsError:
            print('Книга с таким названием уже существует.')
            return False

    def delete_book(self, name_book):  # Функция удаления книги
        try:
            book_path = self.book_path / name_book  # Проверка на существование требуемой для удаления книги
            shutil.rmtree(book_path)  # Удаление книги
        except FileNotFoundError:
            print('Такой книги не существует')
            return False

    def chenge_name(self, name_book, new_name_book):  # Функция по смене названия книги
        book_path = self.book_path / name_book
        book_info_path = book_path / 'info.txt'
        with open(book_info_path, 'r', encoding='utf-8') as info1:
            lines = info1.readlines()
            lines[1] = ' Название книги: ' + new_name_book + '\n'
        with open(book_info_path, 'w', encoding='utf-8') as info2:
            for line in lines:
                info2.write(line)
        try:  # Проверка на существование книги у которой необходимо переменовать название
            old_path = self.book_path / name_book
            new_path = self.book_path / new_name_book
            os.rename(old_path, new_path)  # Смена названия книги
        except FileNotFoundError:
            print('Такой книги не существует')
            return False

    def full_info(self):  # Функция для вывода всей информации
        for dir in self.book_path.iterdir():
            info_dir = dir / 'info.txt'
            with open(info_dir, 'r', encoding='utf-8') as info:
                print(info.read())
            print('\n')
