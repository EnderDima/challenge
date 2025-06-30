def vowels(word, a=0):
    liter = ['а','е','ё','и','о','у','ы','э','ю','я']
    a = 0
    for x in word:
        if x in liter:
            a = a + 1
    return a

world = input('Введите слово: ')
print('Число гласных букв: ', vowels(world))
