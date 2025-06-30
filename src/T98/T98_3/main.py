
i = int(input('Введите ваш возраст: '))

print('Вы внесены в группу - ', end = '')
if i <= 12:
    print('Дети')
elif i > 12 and i <= 18:
    print('подростки')
elif i > 18 and i <= 27:
    print('клуб 27')
elif i > 27 and i <= 45:
    print('молодые')
elif i > 45 and i <= 60:
    print('зрелые')
elif i > 60 and i <= 74:
    print('пожилые')
elif i > 74 and i <= 90:
    print('молоды в душе')
elif i > 90:
    print('долгожитель')
else: print('Error')

