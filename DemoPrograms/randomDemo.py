import DiceThrow

for i in range(5):
    print(DiceThrow.randrange(10), end=" ")
print()

for i in range(5):
    print(DiceThrow.randint(50, 70), end=" ")
print()

# To pick a element randomly from list of elements

members = ['John', 'Smith', 'Bob', 'Andy', 'Tom', 'Jerry']
leader = DiceThrow.choice(members)
print(f'Leader is {leader}')
