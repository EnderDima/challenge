massiv_str = input('Введите массив числе через пробел ' + '') 
massiv = [int(x) for x in massiv_str.split()]

length = len(massiv)
massiv_inv = []
a = 0
for x in massiv:
    a = a + 1
    massiv_inv.append(massiv[length - a])

print(massiv_inv)
