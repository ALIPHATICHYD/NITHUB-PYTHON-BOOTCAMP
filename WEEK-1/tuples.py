# Tuples in Python
# Tuple is a type of data structure, it's a container where we can store different values. It is similar to lists where we can store multiple pieces of information. But Tuple has few key differences from lists. Tuples are immutable, it means they cant be modified once they are created. We can't add or remove items from tuples. Tuples are represented by parenthesis ().


# Creating a Tuple

coordinates = (4, 5)
coordinates[1] = 10 # When trying to assign a new number to the element in the tuple, it will throw an error as tuples are immutable

print(coordinates[0]) # To access the first element of the tuple