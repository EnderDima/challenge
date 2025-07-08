from contextlib import suppress
from pathlib import Path
import random as r

def clothing_selection(temperature):
    i = 0
    data_path = Path(__file__).parent
    data_path = data_path / 'data'
    clothe = []
    clothes = {}
    for item in data_path.iterdir():
        for item_item in item.iterdir():
            file_name = item_item.name
            temperature_min, temperature_max = file_name.split(' - ')
            temperature_max, _bag = temperature_max.split('(')
            if int(temperature_min) <= int(temperature) and int(temperature_max) >= int(temperature):
                clothe.append(file_name)
                i += 1
        with suppress(IndexError, ValueError, UnboundLocalError):
            clothes.update({ item : clothe[r.randint(0,i-1)]})
        clothe = []
        i = 0
    for path_type, path_file in clothes.items():
        path_full = path_type / path_file
        with open(path_full, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(f'{lines[0].strip()} ({lines[1].strip()}) - Temperature = {lines[2].strip()}')
    if clothes == {}:
        return 'Подходящей одежды нет:'
    return ''
def create_clothes(name_clothe, type_clothe, temperature_min_clothe, temperature_max_clothe):
    temperature_clothe = str(temperature_min_clothe) + ' - ' + str(temperature_max_clothe)
    id = 0
    data_path = Path(__file__).parent
    data_path = data_path / 'data' / type_clothe
    data_path.mkdir(parents=True, exist_ok=True)
    id = 0
    while True:
        file_name = f'{temperature_clothe}({id}).txt'
        file_path = data_path / file_name
        if not file_path.exists():
            break
        id += 1
    with open(file_path, 'a', encoding='utf-8') as data:
        data.write(name_clothe + '\n' )
        data.write(type_clothe + '\n')
        data.write(temperature_clothe + '\n')
while True:
    print('1 - поборать одежду')
    print('2 - добавить одежду')
    print('Любая другая клавиша для выхода')
    choice = input('Выбор действия: ')
    if choice == '1':
        temperature = input('Какая температура на улице: ')
        print('Сегодня желательно надеть:')
        print(clothing_selection(temperature))
    elif choice == '2':
        name = input('Введите название вещи: ')
        type_ = input('Введите тип вещи: ')
        temperature_min = input('Введите минимальную температуру: ')
        temperature_max = input('Введите максимальную температуру: ')
        create_clothes(name, type_, temperature_min, temperature_max)
    else:
        break
