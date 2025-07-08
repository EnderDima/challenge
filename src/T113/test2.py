def max_digit(input_number):
    output_number = 0 
    for n in str(input_number):
        try:
            if output_number < int(n):
                output_number = int(n)
        except ValueError:
            output_number = False 
    return output_number

number = input('Введите число: ')
if not max_digit(number):
    exit()
print('Максимальная цифра равна : ', end='')
print(max_digit(number))