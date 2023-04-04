# The Type() Function
# The type() function returns the type of the object passed to it.
# If the object is a class, then the type of the class is returned.

# Example 1: How type() works in Python?

type(5)
print(type(5))

# Result in terminal >> <class 'int'>  
# The int there is the Integer.


# Boolean Data Type

print(5 == 5)
# Result in terminal >> True.

print(5 == 2)
# Result in terminal >> False


print(type(5 == 2))
# Result in terminal >> <class 'bool'>
# The bool there indicates that the datatype is a boolean.


# The bool() function
print(bool("abc"))


# Numbers
# In Python we have data types to handle numbers:
# Integers int()
# Float float()
# Complex complex()

print(type(5.1))
# Result in terminal >> <class 'float'>

int(5)
float(5)

# Type Conversion
# We can convert between types by using different type conversion functions like int(), float(), str(), etc.
# For example

print(int("1"))

