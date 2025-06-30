print('Введите пароль:', end='')
pasword = input()
print('Введите пароль повторно:', end='')
paswordRepit = input()
if pasword == paswordRepit:
    print('Поздравляю вы зарегистрировались')
else: print('Ошибка! Пароли не совпадают')