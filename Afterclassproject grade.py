
grades = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "Daisy": 65,
    "Ethan": 78}

total = 0

for score in grades.values():
    total += score

print("Class average:", total / len(grades))

highest = 0

for score in grades.values():
    if score > highest:
        highest = score

print("Highest score:", highest)

name = input("Enter a student's name: ")

print("Student score:", grades.get(name, "Student not found"))
