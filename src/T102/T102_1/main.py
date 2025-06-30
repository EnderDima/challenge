
def forma(data, message):
    chapter = '\n' + data + '\n' + message
    return chapter

data = input('Введите сегоднешнюю дату: \n ')
message = input('Введите ваше сообщение: \n ')
message += '\n'

file = open('book/diary.txt', 'a', encoding='utf-8')
file.write(forma(data, message))
file.close()

file = open('book/diary.txt', 'r', encoding='utf-8')
for word in file:
    print(word)
file.close()