# Write a Python program to iterate over sets.


# set with integer datatypes
a = {12,32,46,65,23}

# function to iterate the set
def iterate():
    for i in a:
        print(i)

def main():
    try:
        print(f"The iteration of sets are : ")
        iterate()
    # handles the error
    except Exception as e:
        print("Error occurred.", e)


if __name__ == "__main__":
    # starting point of the program
    main()