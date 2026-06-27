# takes input from user
s = input("Enter two strings separated by a comma: ")
# seperates strings using split function
a, b = s.split(",")
a = a.strip()
b = b.strip()
# create new varaibles and swap characters
new_a = b[:2] + a[2:]
new_b = a[:2] + b[2:]
# print new character
print(f"{new_a} {new_b}")