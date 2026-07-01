# Write a Python program to map two lists into a dictionary.


# frist list as a key in dictionary
list_1 = [1,2,3,4,5]
# second key as a value iin dictionary
list_2 = ["apple", "banana", "grapes", "mango", "peach"]

# function to map both lists
def mapping(list_1, list_2):
    result = dict(zip(list_1, list_2))
    return result

def main():
    try:
        final = mapping(list_1, list_2)
        print(f"The mapping list are in the form of dictionary is : {final}")

    # handles the invalid input
    except:
        print("Invalid input! Pleas enter the valid input.")

if __name__ == "__main__":
    # staring point of program
    main()