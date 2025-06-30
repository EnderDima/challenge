loop = True
loop_2 = True
loop_3 = True

while loop:   
    try:
        x = int(input('Введите число 1: '))
        loop = False
    except ValueError:
        print('Ошибка, введите число!')

while loop_2:   
    try:
        y = int(input('Введите число 2: '))
     
        try:
            print(x/y)
            loop_2 = False
        except ZeroDivisionError:
            print('Ошибка, на ноль делить нельзя')
        
    except ValueError:
        print('Ошибка, введите число!')


