def bank(N,yers):
    i = 0
    percent = 0.1
    while i != yers:
        i = i + 1
        N = N + N*percent
    return(int(N))

N_user = int(input('Сколько у вас денег? \n '))
yers_user = int(input('На сколько лет хотите внести вклад? \n '))
print('По итогу вы получите ', bank(N_user,yers_user), ' рублей')