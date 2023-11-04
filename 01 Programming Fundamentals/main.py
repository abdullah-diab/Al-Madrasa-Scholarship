print("Hello World!")

# challenge 01
first_num = int(input("Insert your first number: "))
second_num = int(input("Insert your second number: "))
operator = str(input("Insert the operation: ")) # By defualt it's a string

if operator == "+":
    print(first_num + second_num)
elif operator == "-":
    print(first_num - second_num)
elif operator == "*":
    print(first_num * second_num)
elif operator == "/":
    print(first_num / second_num)
else:
    print("Invalid operator")
  
print("Thanks for using our software :)")


# challenge 02
def calculate(a, b, c):
  return (a + b) * c
print(calculate(1, 2, 3))
print(calculate(2, 3, 4))
print(calculate(3, 4, 5))