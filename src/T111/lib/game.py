from .interface import Interface

class Game(Interface):
    def __init__(self):
        super().__init__()
        self.check_word = self.get_word()
        self.error = False
    def check_letter(self, letter):
        word = self.check_word
        print(word)
        id = -1
        letter = letter.upper()
        letter_number = []
        for lett in word:
            id = id  + 1
            if letter == 'Ё':
                letter = 'Е'
            if letter == 'Й':
                letter = 'И'
            if lett == letter:
                letter_number.append(id)
        if not self.interface_string(letter_number, letter):
            self.error = True
    def check_error(self):
        if self.error:
            self.error = False
            return True
        return None
    def check_win(self):
        number2 = 0
        number = -1
        for _letter in self.word:
            number = number + 1
        for letter2 in self.letter:
            if letter2 != "__ ":
                number2 = number2 + 1
        if number == number2:
            return True
        return None
