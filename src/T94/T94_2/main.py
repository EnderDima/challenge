print('Введите оценку:', end='')
score = float(input())
if 5 >= score >= 4.5:
    print('отлично ⭐⭐⭐⭐⭐')
elif 4.5 > score >= 3.5:
    print('хорошо ⭐⭐⭐⭐')
elif 3.5 > score >= 2.5:
    print('нормально ⭐⭐⭐')
elif 2.5 > score >= 1.5:
    print('плохо ⭐⭐')
elif 1.5 > score >= 0:
    print('ужастно ⭐')
else: print('Оценка введина не кореrтно')  