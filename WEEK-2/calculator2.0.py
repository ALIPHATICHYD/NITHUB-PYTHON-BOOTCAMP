# Building a Better Calculator 

# First thing to do is to get input from the user. Three variables will be created. One for the First Number, One for the Second Number and One for the Operator. So we basically store the values that the user inputs into those variables.

num1 = float(input("Enter first number: ")) # Enter the value for the First Number

op = input("Enter Operator: ") # Enter Operator

num2 = float(input("Enter your second number: ")) # Enter the value for the Second Number 

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")