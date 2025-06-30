array = list(range(300))
arrey_even = []
arrey_uneven =[]

for i in array:
    if i%2 == 0:
        arrey_even.append(i)
    else:
        arrey_uneven.append(i)

print(array)
print(arrey_even)
print(arrey_uneven) 