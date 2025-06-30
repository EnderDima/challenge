base = {}
Id = {}
id = 0
print('Добро пожаловать в наше приложение')
while True:
    choice = input('Ведите 1, чтобы зарегистрироваться \n Введите 2, чтобы авторизироваться \n Введите 3, для смены пароля \n')
    print(base)
    if choice == '1':
        print('Процесс регистрации')    

        login = input('Введите логин: \n')
        if login in base:
            print('Такой логин уже существует')
            continue

        password = input('Введите пароль: \n')
        if password == '' or password.find('#'):
            print('Пароль не может быть пустой стракой или содержать #!')
            continue

        password_again = input('Введите пароль поаторно: \n')
        if password == password_again:
            base[login] = password
            print('Процесс регистрации прошёл успешно')
            print(base)
            Id[login] = id + 1
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
            
            a = 3
            while a != 0:
                password = input('Введите пароль: \n')
                a = a - 1
                if password == base[login]:
                    print('Вы успешно вошли в систему')
                    break
                else:
                    print('пароль не верный. осталось ', a, 'попыток')
                    continue
            else: break
        else:
            print('Такой пользователь не зарегистрирован')
            continue
    elif choice == '3':
        print('Процесс смены пароля') 

        login = input('Введите логин: \n')
        if login in base:
            
            a = 3
            while a != 0:
                password = input('Введите пароль: \n')
                a = a - 1
                if password == base[login]:
                    print('Вы успешно ввели старый пароль. Теперь ведите новый пароль: \n')
                    new_password = input()
                    if new_password == '' or new_password.find('#'):
                        print('Пароль не может быть пустой стракой!')
                        continue
                    password_again = input('Введите пароль поаторно: \n')
                    if new_password == password_again:
                        base[login] = new_password
                        print('Процесс регистрации прошёл успешно')
                        print(base)
                    elif new_password != password_again:
                        print('Пароли не совпадают')
                        continue
                    print('Вы успешно сменили пароль')
                    break
                else:
                    print('пароль не верный. осталось ', a, 'попыток')
                    continue
            else: break
        else:
            print('Такой пользователь не зарегистрирован')
            continue
    
    else:
        print('Выход из системы')
        break
