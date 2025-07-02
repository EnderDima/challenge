from pathlib import Path
from .lib import Lib
import os

class Book(Lib):
    def __init__(self, book):
        Lib.__init__(self)
        self.book = book
        self.book_path = self.elektron_lib_path / book
    def choose_book(self): # Фунция проверки существования редактируемой книги
        base_dir = self.book_path
        if base_dir.exists():
            print("Книга выбрана: " + str(self.book))
            return(True)
        print("Такой книги нет")
        return False
    def add_chapter(self, name_chapter): # Функция добавления главы в книгу
        number = 0
        base_dir = Path(__file__).parent.parent
        elektron_lib_path = base_dir/ 'elektron_lib'
        elektron_lib_path.mkdir(exist_ok=True)
        book_path =  self.book_path / name_chapter
        book_info_path = self.book_path / 'info.txt'
        with open(book_path, 'w', encoding="utf-8") as info:
            info.write(" ")
        for _item in os.listdir(self.book_path): # Смена информации о колличестве глав в файле с информацией
            number = number + 1
        with open(book_info_path, 'r', encoding="utf-8") as info1:
            lines = info1.readlines()
            lines[2] = 'глав в книге ' + str(number)
        with open(book_info_path, 'w', encoding="utf-8") as info2:
            for line in lines:
                info2.write(line)
    def delete_chapter(self,name_chapter):  #  Функция удаления главы
        number = 0
        base_dir = Path(__file__).parent.parent
        elektron_lib_path = base_dir/ 'elektron_lib'
        elektron_lib_path.mkdir(exist_ok=True)
        try: # Проверка существования желаймой к удалению главы
            book_path = self.book_path / name_chapter
            book_info_path = self.book_path / 'info.txt'
            os.remove(book_path)
            for _item in os.listdir(self.book_path): # Смена информации о колличестве глав в файле с информацией
                number = number + 1
            with open(book_info_path, 'r', encoding="utf-8") as info1:
                lines = info1.readlines()
                lines[2] = 'глав в книге ' + str(number-1)
            with open(book_info_path, 'w', encoding="utf-8") as info2:
                for line in lines:
                    info2.write(line)
        except FileNotFoundError:
            print("Такой главы не существует")
            return False
    def chenge_chapter(self, name_chapter, new_name_chapter): # Функция смены названия главы
        base_dir = Path(__file__).parent.parent
        elektron_lib_path = base_dir/ 'elektron_lib'
        elektron_lib_path.mkdir(exist_ok=True)
        try: # Проверка на существование главы у которой необходимо переменовать название
            old_path = self.book_path / name_chapter
            new_path = self.book_path / new_name_chapter
            os.rename(old_path, new_path)
        except FileNotFoundError:
            print("Такой главы не существует")
            return False
