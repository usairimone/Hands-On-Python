# Write a Python program to reverse a string.


def reverse(str):
    # reverse the string.
    return str[::-1]

def main():
    try:
        str = input("Enter the string : ")
        print(reverse(str))
    # handles the invalid input,
    except:
        print("Invalid input!")

# starting point of the program.
if __name__ == "__main__":
    main()