numbers = [-34, -56, -78, -12, -45, -99, -56]
temp = numbers[0]
for num in numbers:
    if temp < num:
        temp = num

print(temp)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    print(*row, sep=",")

for row in matrix:
    for item in row:
        print(item)
