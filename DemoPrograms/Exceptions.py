try:
    age=int(input("Enter age: "))
    income=10000
    risk=income/age
    print(f'Age is :{age}')
    print(risk)
except ZeroDivisionError:
    print('Age cannot be "0"')
except ValueError:
    print('Invalid value..')