fruits = [
    'apples',
    'bananas',
    'grapes',
    'mangos',
    'nectarines',
    'pears',
    'watermillion',
]

print("I love eating these fruits:")

for fruit in fruits:
    print(fruit.capitalize())

print("------------------------")

counter = 0
while fruits[counter] != "nectarines":
    print(fruits[counter])
    counter += 1

print("------------------------")

for fruit in fruits:
    if fruit != "nectarines":
        print(fruit.capitalize())

print("------------------------")

for fruit in fruits:
    if fruit == "nectarines":
        break
    print(fruit.capitalize())