base = {}

print('Добро пожаловать в наше приложение')
while True:
    choice = input('Ведите 1, чтобы зарегистрироваться \n Введите 2, чтобы авторизироваться \n Введите 3, чтобы выйти из приложения')
    print(base)
    if choice == '1':
        print('Процесс регистрации')    

        login = input('Введите логин: \n')
        if login in base:
            print('Такой логин уже существует')
            continue

        password = input('Введите пароль: \n')
        if password == '':
            print('Пароль не может быть пустой стракой!')
            continue

        password_again = input('Введите пароль поаторно: \n')
        if password == password_again:
            base[login] = password
            print('Процесс регистрации прошёл успешно')
            print(base)
        elif password != password_again:
            print('Пароли не совпадают')
            continue
        else: 
            print('Error!')
            break
    
    elif choice == '2':
        print('Процесс авторизации') 

        login = input('Введите логин: \n')
        if login in base:
            password = input('Введите пароль: \n')
            if password == base[login]:
                print('Вы успешно вошли в систему')
                continue
            else:
                print('пароль не верный')
                continue
        else:
            print('Такой пользователь не зарегистрирован')
            continue
    else:
        print('Выход из системы')
        break
