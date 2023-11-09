firstNumber = int(input("Please insert your first number: "))
secondNumber = int(input("Please insert your second number: "))
operation = input("Please insert the operation you want to perform: ")

if operation == "+":
    print("result is:", firstNumber + secondNumber)
elif operation == "-":
    print("result is:", firstNumber - secondNumber)
elif operation == "*":
    print("result is:", firstNumber * secondNumber)
elif operation == "/":
    print("result is:", firstNumber / secondNumber)
else:
    print("This operation is not supported. Supported operations are: + - * /")

print("Thanks for using our software")