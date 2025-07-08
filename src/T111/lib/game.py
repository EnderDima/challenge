from .interface import Interface


class Game():
    def __init__(self, letter):
        super().__init__()
        self.check_word = Interface.get_word()
        self.error = False
        self.letter = letter
    def check_letter(self, letter):
        word = self.check_word
        id = -1
        letter = letter.upper()
        letter_number = []
        for lett in word:
            id = id + 1
            if letter == "Ё":
                letter = "Е"
            if letter == "Й":
                letter = "И"
            if lett == letter:
                letter_number.append(id)
        if not Interface.interface_string(letter_number, letter):
            self.error = True
    def check_error(self):
        if self.error:
            self.error = False
            return True
        return None
    def check_win(self):
        number2 = 0
        number = -1
        for _letter in self.check_word:
            number = number + 1
        for letter2 in Interface(self.letter):
            if letter2 != "__ ":
                number2 = number2 + 1
        if number == number2:
            return True
        return None
