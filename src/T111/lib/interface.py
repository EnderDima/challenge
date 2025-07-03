import random
from pathlib import Path

class Interface():
    def __init__(self):
        base_dir = Path(__file__).parent.parent
        words_path = base_dir/ 'words.txt' 
        random_word_number = random.randint(1,10)
        with open(words_path, 'r', encoding="utf-8") as word:
            random_word = word.readlines()
            self.word = random_word[random_word_number].upper()
            word.close()
            letters = []
            print(random_word[random_word_number]) 
            for letter in random_word[random_word_number]:
                if letter.strip():
                    letters.append('__ ')
            self.letter = letters
    def get_word(self):
        return(self.word)
    def interface_string(self, number_letter, letter2):
        if number_letter == []:
            for lett in self.letter:
                print(lett, end = " ")
            return False
        else:
            for number, letter in enumerate(self.letter):
                for number2 in number_letter:
                    if number2 == number:
                        self.letter[number] = letter2
            for lett in self.letter:
                print(lett, end = " ")
    def interface_figure(self, number_error):
        base_dir = Path(__file__).parent.parent
        fig_dir_path = base_dir/ 'fig'
        fig_path =fig_dir_path / f"{number_error}.txt"
        print('\n')
        with open(fig_path, 'r', encoding="utf-8") as fig:
            lines = fig.readlines()
            for line in lines:
                print(line, end = '')
