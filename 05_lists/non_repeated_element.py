# Write a Python program to find the first non-repeated element in a list.


# list with intger collection of data
li = [12, 5, 8, 12, 3, 5, 19, 8, 7, 3, 25, 12, 7, 30, 5, 18, 25, 8, 3, 12]

# function to find first non-repeated element
def non_repeated(li):
    for i in li:
        if li.count(i) == 1:
            return i
    return None

def main():
    try:
        result = non_repeated(li)
        # using helper function
        if result is not None:
            print(f"The first non-repeated element is : {result}")
        else:
            print("This is no non-repeated element.")
    except:
        print("Invalid input! Please enter valid input.")

if __name__ == "__main__":
    # starting point of the program
    main()