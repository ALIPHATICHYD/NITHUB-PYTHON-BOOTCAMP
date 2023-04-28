students = {
    "aliphatic": ["ALIPHATIC", "HYDROCARBON", "MALE"],
    "aromatic": ["AROMATIC", "HYDROCARBON", "FEMALE"] 

    "total_number": 3}


print(students)

# students.update({"total_number": 4})

# print("\n\n")
print(students.setdefault("age", 100))

print(students)