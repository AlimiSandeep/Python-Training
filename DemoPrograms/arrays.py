cart = [10, 20, 30, 40]
sum = 0;
for item in cart:
    sum += item
print(f'Total price = {sum}')
print(*cart, sep=",")
# print(",".join(cart))


arr = [str(a) for a in cart]
print(",".join(arr))


number=[5,2,5,2,2]
for i in range(len(number)):
    for j in number:
        print('x' * j)

