weight=int(input('Enter weight:'))
option=input(f"(L)bs or (K)gs")
if option=='L' or option=='l':
    print(weight*0.45)
elif option.upper()=='K':
    print(round(weight/0.45))
else:
    print("invalid input")