from .interface import Interface

class Game(Interface):

    def __init__(self):
        super().__init__()
        self.check_word = self.word
        self.error = False

    def check_letter(self, letter):
        word = self.check_word
        print(word)
        id = 0
        error = 0
        for letterW in word:
            id = id + 1
            if letter == letterW:
                self.interface_string(1, letter)
                return
            else: 
                error = error + 1
                if id == error: self.interface_string(2, letter)
        if error == id:
            self.error = True
    
    def check_error(self):
        if self.error == True:
            self.error = False
            return(True)