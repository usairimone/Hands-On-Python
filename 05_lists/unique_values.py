# list with integer datatypes.
li = [12, 5, 8, 12, 3, 5, 19, 8, 7, 3, 25, 12, 7, 30, 5, 18, 25, 8, 3, 12]

# function to find unique elements by using set.
def unique_elements(li):
    unique = set(li)
    return unique


def main():
    # prints the unique elements
    try:
        result = unique_elements(li)
        print(f"The unique values from a list is : {result}")
    # handling the invalid input.
    except:
        print("Invalid input! Please enter the valid input.")

if __name__ == "__main__":
    # starting point of the program
    main()