# Functions in Python 
# Functions are basically just a collection of code that performs a particular task. It helps us to organize our code and make it reusable. We can call a function as many times as we want. We can also pass data to a function, which is called parameters. We can also return data from a function, which is called a return value. We can also create a function without a name, which is called an anonymous function or lambda function.

# Creating a Function

def say_wagwan(name, age):
    print("Wagwan " + name + ", you are "  + age + " innit?")

say_wagwan("ALPHA", "21")
say_wagwan("BETA", "17")

# You can really pass any type of data 



# Return Statement
# The Return Keyword can basically allow Python to return information from a function.

def cube(num):
    return num*num*num

print(cube(3))