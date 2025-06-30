basket = ['молоко', 'курица', 'хлопья','картошка','помидоры']
print('в магазине необходимо купить - ', end='')
print(*basket, sep=(', '))
buys = []
while len(basket) > len(buys):
    buy = input('Введите то что вы купили (или напишите стоп для завершения покупок): ' + '')
    if buy == "стоп":
        break

    if buy in basket and buy not in buys:
        buys.append(buy)
        print('Прекрасно вы купили - ', buy)

        remains = [x for x in basket if x not in buys]
        
        if remains:
            print('осталось купить: ', end='')
            print(*remains, sep=(', '))
        
    elif buy in buys:
        print('Это уже куплено')
    else: 
        print('Такого тавара нет в списке. Осталось купть: ', end='')
        print(*remains, sep=(', '))

if len(basket) == len(buys):
    print('Всё куплено') 
elif len(buys) > 0:
    print('Что то куплено, но к сожелению не всё')
else: print('Ничего не куплено')
