import random

number_random  = random.randint(0,15)

print('Загадано число от 0 до 15, отгадайте какое за 3 попытки?')
counter = 0
while counter < 3:
    try:
        number = int(input())
    except ValueError:
        print("Неверный ввод")
        break
    
    if number == number_random:
        print('Ура вы выйграли')
        break
    elif abs(number - number_random) > 2:
        counter = counter + 1
        if number - number_random > 0:
            print('Холодно (Нужно меньше)')
        else: print('Холодно (Нужно больше)')
        continue
    elif abs(number - number_random) <= 2:
        counter = counter + 1
        if number - number_random > 0:
            print('Тепло (Нужно меньше)')
        else: print('Тепло (Нужно больше)')
        continue
    else: 
        print('Error')
        break
else: print('Неудача вы использовали все опытки. Загданое число - ', number_random)