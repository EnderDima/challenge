import sys


def max_digit(input_number):
    output_number = 0
    for n in str(input_number):
        try:
            output_number = max(output_number, int(n))
        except ValueError:
            output_number = False
    return output_number

number = input('Введите число: ')
if not max_digit(number):
    sys.exit()
print('Максимальная цифра равна : ', end='')
print(max_digit(number))
