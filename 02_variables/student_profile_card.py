# initialize name, age, height, grade, and is_class_monitor variables
name = "Muhammad Usairim"
age = 20
height = 5.6
grade = "B"
is_class_monitor = True

# use the variables to print a formatted student profile card
title = "Student Profile Card"
print(f"{title:-^60}")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Grade: {grade}")
print(f"Class Monitor: {'Yes' if is_class_monitor else 'No'}")