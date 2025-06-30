message = input('Введите ваше сообщение: \n ')
message += '\n'

file = open('files/text.txt', 'a', encoding='utf-8')
file.write(message)
file.close()

file = open('files/text.txt', 'r', encoding='utf-8')
for word in file:
    print(word)
file.close()