# Write a Python program to get a single string from two given strings, separated by a space, and swap the first two characters of each string.


# take two strings as input.
s = input("Enter two strings separated by a comma: ")

# split input into two strings.
a, b = s.split(",")

# remove extra spaces.
a = a.strip()
b = b.strip()

# swap first two characters.
new_a = b[:2] + a[2:]
new_b = a[:2] + b[2:]

# display result.
print(f"{new_a} {new_b}")