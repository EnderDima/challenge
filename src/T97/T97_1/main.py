FIO = []

def initials(FSc):
    print(FSc[0], FSc[1][0] + '.' +  FSc[2][0] + '.')


surname = input('Введите фамилию:\n ')
name = input('Введите Имя: \n ')
postname = input('Введите отчество: \n ')
FIO.append(surname)
FIO.append(name)
FIO.append(postname)
print('Ваше ФИО сокращено:')
initials(FIO)
