# Write a Python program to sort a dictionary by value in:
# Ascending order
# Descending order


# dictonary with string values.
dictionary = {
    3 : "ali",
    1 : "usairim",
    2 : "ahmad"
}
# dictionary before sorting.
print("Dictionary before sorting:", dictionary)

# Ascending.
asc = sorted(dictionary.items(), key=lambda x: x[0])
print("Ascending:", asc)

# Descending.
desc = dict(sorted(dictionary.items(), key=lambda x: x[0], reverse=True))
print("Descending:", desc)