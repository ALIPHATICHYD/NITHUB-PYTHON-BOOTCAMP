"""
Task: Pring from 1 - 100 
"""

counter = 100

while True: 
    print(101 - counter)
    counter -= 1
    print()


"""
Task: Multiples of 7 between 1 and 1000
"""

counter = 1000

while counter >= 1:
    if counter % 7 == 0:
        print(counter)

    else:
        print("Not a multiple of 7")

    counter -= 1