name_men = ['Ваня','Петя','Вова']
name_women = ['Маша','Даша','Таня']
name = []
name.extend(name_men)
name.extend(name_women)
print('мужкие имена - ', end='')
print(*name_men, sep=(', '))
print('женские имена - ', end='')
print(*name_women, sep=(', '))
name.sort()
print('все имена по алфавиту - ', end='')
print(*name, sep=(', '))
