def print_file(file_name):
    for w in file_name:
        print(w)

def create_file(file_name):
    file = open(file_name, 'w', encoding='utf = 8')
    return file

if __name__ == '__main__':
    print('Привет это  мой первый модуль')