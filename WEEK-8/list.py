## Squaring Numbers From 1 to 5

squares = [x**2 for x in range(1, 6)]
print(squares)
# Output: [1, 4, 9, 16, 25]


## Filtering Even Numbers From A List

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens)
# Output: [2, 4, 6, 8, 10]


## Generating A List Of Uppercase 

message = "Hello, World!"
upper_letters = [char for char in message if char.isupper()]
print(upper_letters)
# Output: ['H', 'W']


# Combining Elements From Two Lists

numbers = [1, 2, 3]
letters = ['A', 'B', 'C']
combined = [(x, y) for x in numbers for y in letters]
print(combined)
# Output: [(1, 'A'), (1, 'B'), (1, 'C'), (2, 'A'), (2, 'B'), (2, 'C'), (3, 'A'), (3, 'B'), (3, 'C')]
 

# List comprehensions are a concise and efficient way to create new lists, and they can often replace the need for explicit loops. However, it's important to use them judiciously to maintain code readability and understandability.