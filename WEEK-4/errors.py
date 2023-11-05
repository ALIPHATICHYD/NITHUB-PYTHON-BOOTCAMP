# Try Except: Catching Errors In Python

try:
    answer = 10/10
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input") 