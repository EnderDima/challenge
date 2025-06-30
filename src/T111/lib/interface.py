import random
from pathlib import Path

class Interface():

    def __init__(self):
        base_dir = Path(__file__).parent.parent
        words_path = base_dir/ 'words' # Переход в директорию электронной библиотеки
        random_word_number = random.randint(1,10)
        words_file = words_path / f"{random_word_number}.txt"
        with open(words_file, 'r', encoding="utf-8") as word:
            random_word = word.read()
            self.word = random_word
            word.close()
            self.letter = []
    
    def get_word(self):
        return(self.word)

    def interface_string(self, id, letter2):
        number_letter = 0
        word = []
        for letter in self.word:
            number_letter = number_letter + 1
            word.append(letter.upper())
        if id == 1:
            for lett in self.word:
                if lett == letter2:
                    self.letter.append(lett)
                    print(lett, end = " ")
                else: print("__ ", end = " ")
        elif id == 2: 
            for lett in self.word:
                if lett in self.letter:
                    self.letter.append(lett)
                    print(lett, end = " ")
                else: print("__ ", end = " ")

        


    def interface_figure(self, number_error):
        base_dir = Path(__file__).parent.parent
        fig_dir_path = base_dir/ 'fig' # Переход в директорию электронной библиотеки
        fig_path =fig_dir_path / f"{number_error}.txt"
        print('\n')
        with open(fig_path, 'r', encoding="utf-8") as fig:
            lines = fig.readlines()
            for line in lines:
                print(line, end = '')



