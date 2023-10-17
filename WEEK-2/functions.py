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
    return num*num*num # This will return the value of num*num*num


result = cube(3)
print(result)



# If Statements 
# If statements are used to check conditions and change the behavior of the program accordingly. If the condition is true, the code inside the if statement will be executed. If the condition is false, the code inside the if statement will not be executed. We can also use else and elif statements to check for multiple conditions. We can also use comparison operators to compare two values. We can also use logical operators to combine multiple conditions.

# An Example of a Basic If Statement
# I wake up
# If I'm hungry 
#     I eat breakfast

# I leave my house 
# If it's cloudy 
#     I bring an umbrella
# otherwise
#     I bring sunglasses

# I'm at a restaurant
# If I want meat
#     I order a steak
# otherwise if I want pasta
#     I order spaghetti & meatballs
# otherwise
#     I order a salad.

# Creating a Boolean Variable

is_male = True

if is_male:
    print("You are a male")
else:
    print("You are not a male")