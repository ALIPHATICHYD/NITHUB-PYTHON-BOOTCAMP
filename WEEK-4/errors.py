# Uncomment the code below to see the output.

# Try Except: Catching Errors In Python

# try:
#     answer = 10/10
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("Invalid Input")   




# Opening Files in Python

## open("errors.txt", "w", "r", "a", "r+") # "w" means write, "r" means read,"a" means append, "r+" means read and write


# errors_file = open("errors.txt", "r")
# for errors in errors_file.readlines():
#     print(errors)  # Read all lines in the file 

# print(errors_file.readable()) # Check if file is readable
# print(errors_file.readline()) # Read the first line

# errors_file.close() # Close the file