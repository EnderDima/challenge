from lib import Game
from lib import Interface

game = Game()
in_fa = Interface()

print("Добро пожаловать в игру!  Вам необходимо угадать слово за 7 попыток.")
loop = True
game.interface_string(1, 0)
game.interface_figure(0)
error = 7
error_letter = []
while loop == True:
    letter = input("Введите букву: ")
    game.check_letter(letter)
    if game.check_error() == True:
        error = error - 1
        error_letter.append(letter)
    game.interface_figure(7 - error)
    print('Ошибки (' + str(7 - error) + '): ', end = '')
    print(error_letter)
    print('Осталось ошибок ' + str(error))