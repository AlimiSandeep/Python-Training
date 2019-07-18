array1 = [1, 3, 4, 1, 3, 4, 2, 5, 6, 3, 10]
array2=array1.copy()
new_array = []
for i in range(len(array1)):
    if (array1.count(i) >= 1):
        new_array.append(i)
        array1.remove(i)

temp = []
for i in range(len(array2)):
    if array2[i] not in temp:
        temp.append(array2[i])

print(*new_array, sep=",")
print('----------------------')
print(*temp,sep=",")