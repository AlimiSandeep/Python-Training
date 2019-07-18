class Person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print(f'Hii, this is {self.name}')

person=Person('Sandeep')
print(person.name)
person.greet()

person=Person('John')
person.greet()