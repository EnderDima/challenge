phone = ['айфон 5', 'айфон 6', 'айфон 7', 'айфон 8', 'айфон 16 pro', 'айфон xr', 'айфон 10','айфон 11', 'айфон 12', 'айфон 13']
print('Поздравляю вы выйграли телефон. Для его получения выберите число от 1 до', len(phone), 'и введите его:')
error = 'Ты дурак тебе же сказали число от 1 до 10. Да пошёл ты рыцаря отвлекаешь'
choice_men = int(input())
if 0 < choice_men:
    if choice_men < len(phone)+1:
        print('Вы выйграли -', phone.pop(choice_men - 1))
    else: print(error)
else: print(error)


