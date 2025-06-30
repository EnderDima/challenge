print('Введите чило N, соотвествующие чилу чисел сумма которых выведится на экран')
N = input('N = ' + '')
N = int(N)
row_n = list(range(1, N+1))
print(row_n)
n = 0
if N > 0:
    for x in row_n:
        n = n + x
    print('Сумма чисел равна =', n)
else: print('число должно быть больше 0')
