from pathlib import Path
import os
import shutil

class Lib(): 
    def __init__(self):
        with open(Path(__file__).parent / 'id' , 'r', encoding="utf-8" ) as id:
            self.id = id.read()
        self.elektron_lib_path = Path(__file__).parent.parent / 'elektron_lib'
        self.elektron_lib_path.mkdir(exist_ok=True)
    def add_book(self, name_book): # функция добавления новой книги
        base_dir = Path(__file__).parent.parent
        elektron_lib_path = base_dir/ 'elektron_lib' # Переход в директорию электронной библиотеки
        elektron_lib_path.mkdir(exist_ok=True)
        book_path = elektron_lib_path / name_book
        try:
            book_path.mkdir(exist_ok=False) # проверка на существование одинаковых по названию книг
        except FileExistsError: 
            print("Книга с таким названием уже существует.")
        book_path = elektron_lib_path / name_book / "info.txt" # Создание файла с информацией
        with open(book_path, 'w', encoding="utf-8") as info:
            # Запись данных в файл с информацией
            info.write("Индекс: " + str(self.id) + '\n Название книги: ' + name_book + '\n глав 0') 
        with open(Path(__file__).parent / 'id' , 'w', encoding="utf-8" ) as id:
            self.id = str(int(self.id)+1)
            id.write(self.id)
    def delete_book(self, name_book): # Функция удаления книги
        base_dir = Path(__file__).parent.parent
        elektron_lib_path = base_dir/ 'elektron_lib'
        elektron_lib_path.mkdir(exist_ok=True)
        try:
            book_path = elektron_lib_path / name_book # Проверка на существование требуемой для удаления книги
            shutil.rmtree(book_path) # Удаление книги
        except FileNotFoundError: 
            print("Такой книги не существует") 
    def chenge_name(self, name_book, new_name_book): #  Функция по смене названия книги
        base_dir = Path(__file__).parent.parent
        elektron_lib_path = base_dir/ 'elektron_lib'
        elektron_lib_path.mkdir(exist_ok=True)
        try: # Проверка на существование книги у которой необходимо переменовать название
            old_path = elektron_lib_path / name_book
            new_path = elektron_lib_path / new_name_book
            os.rename(old_path, new_path)      # Смена названия книги
        except FileNotFoundError: 
            print("Такой книги не существует")
    def full_info(self): # Функция для вывода всей информации
        base_dir = Path(__file__).parent.parent
        elektron_lib_path = base_dir/ 'elektron_lib'
        elektron_lib_path.mkdir(exist_ok=True)
        for dir in elektron_lib_path.iterdir():
            info_dir = dir / 'info.txt'
            with open(info_dir, 'r', encoding="utf-8") as info:
                print(info.read())
            print('\n')
