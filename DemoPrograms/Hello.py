from builtins import print

name=input("What is your name ?")
print("Hi "+name)
print(name.upper())
print(name.lower())
print(name[:5])
print(name.capitalize())
print(name.split(" "))
print(name.find('alimi'))
print(name.title())
print('alimi' in name)
temp1=name
temp2=name[:]
print(temp1)
print(temp2)

first='sandeep'
last='alimi'
print(first +' ['+last+']'+' is a coder')

msg=f'{first} [{last}] is a coder'
print(msg)