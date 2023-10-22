# List/Arrays In Python

friends = ["Kero", "Jide", "Walzeem", "Lami", "Teemah"] 
friends[1] = "Jesus" #Modifying values inside of an array/list
print(friends[1])

print(friends[1:3]) # When using range, it will take the element thats up to the value but not that value


# List Functions

lucky_numbers = [1, 0, 8, 9, 7]
friends = ["Kero", "Jide", "Walzeem", "Lami", "Teemah"]

friends.extend(lucky_numbers) # To append a list at the end of another list 

friends.append("Jesus") # To add an element to the end of the list

friends.insert(1, "Jesus") # To insert an element to the list, wherever it is inserted into the array will be pushed to the right 

friends.remove("") # To remove a particular element in the list

friends.clear() # To empty the list

friends.pop() # To remove the last element off the list

lucky_numbers.sort() # To sort out the elements in the list in alphabetical order

lucky_numbers.reverse() # To reverse the order of elements in the list 

friends2 = friends.copy() # Creating a new list and making it a copy of the other list


print(friends.index("Kero")) # To check the index of a particular element in a list

print(friends2)
