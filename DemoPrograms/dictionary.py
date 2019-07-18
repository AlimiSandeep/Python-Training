student = {
    'name': 'sandeep',
    'rollnum': 504,
    'marks': 88
}

print(student["marks"])
print(student.get('name'))
print(student.get('dob'))
print(student.get('dob', 'Not found'))

# Modifying the dictionary
student['name'] = 'Sandeep'
print(student)

# Appending to dictionary
student["dob"] = '9-Nov-1997'
print(student.get('dob'))

print('----------------')

num_to_word = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six'
}
phone_num = (input("Enter your number:"))
number = int(phone_num[::-1])
length = 0
elements = []
while length < len(phone_num):
    rem = number % 10
    elements.append(rem)
    number //= 10
    length += 1

output = ""
for num in elements:
    output += num_to_word.get(num, "!!!!") + " "
print(output)

print("---------------------")

convertor = {
    "1": 'One',
    "2": 'Two',
    "3": 'Three',
    "4": 'Four'
}

num = input('Enter number')

op = ''
for ch in num:
    op += convertor.get(ch, "!!!") + " "
print(op)
