# Write a Python program to check whether a given key exists in a dictionary.


# dictionary with string values
dictionary = {
    1 : "usairim",
    2 : "machine learning engineer",
    3 : "5th semester",
    4 : "ready to work with seniors",
    5 : "passionate to work on real-world projects"
}

# function to check key existence
def existence(dictionary):
    key = int(input("Enter a key to check: "))

    # check existence
    if key in dictionary:
        print("Key already exists in dictionary.")
    else:
        print("Key does not exist in dictionary.")

# prints function
existence(dictionary)