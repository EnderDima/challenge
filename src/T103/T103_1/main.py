loop = True

while loop:
    try: 
        age = int(input('Введите ваш возраст: \n'))
        loop = False
    except ValueError:
        print('Возраст указан не коректно')
print('Ваш возраст: ', age)