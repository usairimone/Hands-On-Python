# Write a Python program to create a dictionary from a given string.


string = "usairim"

# function to count character occurrences.
def count(string):
    result = {}

    # iterate through each character in the string.
    for i in string:
        if i in result:
            result[i] += 1

        # add character with initial count.
        else:
            result[i] = 1

    return result

# main function.
def main():
    try:
        # call the counting function.
        show = count(string)
        print(f"The dictionary from a string is : {show}")

    # handle unexpected errors.
    except:
        print("Invalid input! Please enter a valid input.")

# program entry point.
if __name__ == "__main__":
    main()