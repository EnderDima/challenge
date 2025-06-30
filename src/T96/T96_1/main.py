base = {1 : ['Москва => Петушки', 'Венедикт П. Ефремов', '45 99 505281', '1'], 2 : ['Москва => Питер', 'Пархом В. Хользман', '55 12 487592', '2'], 3 : ['Москва => Пушкино', 'Петр А. Пупкин', '55 12 875426', '3']}

while True:
    choice = input('Введите для просмотра существующих билетов 1 \n для ввода нового билета введите 2 \n' + '')
    if choice == '1':
        print('В базе присутствуют следующие билеты: \n' )
        for key in base.items():
            print('*** место №', key[0], ' ***')
            print('Маршрут: ', key[1][0])
            print('Пассажир: ', key[1][1])
            print('Паспорт:', key[1][2])
            print('Номер билета:', key[1][3], '\n')
    elif choice == '2':
        trail = ''
        FIO = '' 
        pasport = ''
        while trail == '' or FIO == '' or pasport == '':    
            print('Для регистрации нового билета введите следующие данные:')
            trail = input('маршрут: ')
            FIO = input('ФИО: ')
            pasport = input('серия номер паспорта: ')
            if trail == '' or FIO == '' or pasport == '':
                print('Данные не могут быть пустой стракой')
                continue
        x = base.values()
        number = len(x) + 1
        print('Ваше место под номером', number)
        base[number] = [trail, FIO, pasport, number] 
    else: break