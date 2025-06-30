choice_phone = ''
while True:
    phone = ['айфон 5', 'айфон 6', 'айфон 7', 'айфон 8', 'айфон 16 pro', 'айфон xr', 'айфон 10','айфон 11', 'айфон 12', 'айфон 13']
    print('Унас в магазине присутствую следующие телефоны')
    a = 0
    for x in phone:
        a = a + 1
        print(a, ' - ', x)
    print('Выберите модель устройства: \n')
    choice_phone = input()
    if int(choice_phone) <= len(phone) and int(choice_phone) > 0:
        phon = phone[int(choice_phone)-1]
        print('\n Вы выбрали ', phone[int(choice_phone)-1], 'Теперь выберите страну доставки')
        break
    else: 
        print('Номер выбран не коректно')
        continue

while True:
    state = {'Россия':['Москва','Новосибирск','Рубцовск'], 'Казахстан':['Алмота','Астана','Семей'], 'Белорусь':['Минск','Бобруск','Журки'], 'Украина':['Киев','Харьков','Полтава']}
    a = 0
    for x in state.items():
        a = a + 1
        print(a, ' - ', x[0])
    choice_state = input()
    a = 0
    for x in state.items():
        a = a + 1
        if a == int(choice_state):
            stat = x[0]
    if int(choice_state) <= len(state) and int(choice_state) > 0:    
        print('\n Вы выбрали ', stat, 'Теперь напишите ваше имя')
        break
    else: 
        print('Номер выбран не коректно')
        continue

name = input()
print('Выберите город оставки')
while True:
    a = 0
    for x in state[stat]:
        a = a + 1
        print(a, ' - ', x)
    choice_city = input()
    citys = state[stat]
    if int(choice_city) <= len(citys) and int(choice_city) > 0:
        city = state[stat][int(choice_city)-1]
        print('\n Вы выбрали ', state[stat][int(choice_city)-1])
        break
    else: 
        print('Номер выбран не коректно')
        continue

print('Ваш заказ:')
print('Имя - ', name)
print('Страна - ', stat)
print('Город - ', city)
print('Телефон - ', phon)