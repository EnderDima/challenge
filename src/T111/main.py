from lib import Game

game = Game()
print("Добро пожаловать в игру!  Вам необходимо угадать слово за 7 попыток. Выберите действие")
loop = True
loop2 = True
error = 7
error_letter = []
while loop:
    print("1 - Начать игру")
    print('2 - Выйти из игры')
    choise = input('< ')
    if choise == '1':
        game.interface_string([], 'k')
        game.interface_figure(0)
        while loop2:
            if error < 2:
                loop2 = False
            letter = input("Введите букву: ").upper()
            game.check_letter(letter)
            if game.check_error() == True:
                error = error - 1
                error_letter.append(letter)
            try:
                game.interface_figure(7 - error)
            except FileNotFoundError:
                loop2 = False
            print('Ошибки (' + str(7 - error) + '): ', end = '')
            print(error_letter)
            print('Осталось ошибок ' + str(error))
            if game.check_win():
                print('Ура вы выйграли!!! \n\n')
                loop2 = False
    else: loop = False 