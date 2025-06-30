array = list(range(1, 101))
array_2 = []
for i in array:
    if i%3 == 0 and i%5 !=0:
        array_2.append('тыры')
    elif i%5 == 0 and i%3 !=0:
        array_2.append('пыры')
    elif i%3 == 0 and i%5 == 0:
        array_2.append('тыры-пыры')
    else:
        array_2.append(i)

print(array)
print(array_2)