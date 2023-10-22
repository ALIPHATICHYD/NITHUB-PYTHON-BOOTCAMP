# While Loops in Python

# When creating a while loop, the first thing that should be done is creating an integer, this is basically creating a variable that's a number.



# Creating the While Loop 

i = 1
while i <= 100:
    print(i)
    i += 1

print("Done with Loop")








# For Loops in Python

# For loops are used to iterate through a sequence, this sequence can be a list, a dictionary, a tuple, a set, or a string.

# Creating a For Loop

for letter in "ALIPHATIC HYDROCARBON":
    print(letter)

friends = ["Jide", "Kero", "Walzeem"]
for friend in friends:
    print(friend)


for index in range(len(friends)):
    print(index)

for index in range(len(friends)):
    print(friends[index])
    friends[2]



# Exponent Function
# This will basically take two numbers and raise the first number to the power of the second number

# Example of the Exponent Function
print(2**3)

# Creating the Function

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
        return result
    
print(raise_to_power(3,4))