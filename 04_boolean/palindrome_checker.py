# Write a Python function that checks whether a given string is a palindrome (reads the same forward and backward) using boolean values.


# checks palindrome condition
def palindrome(str):
    return (str[0::] == str[::-1])
        

def main():
    # takes string as a input
    str = input("Enter the string: ")
    try:
        # using helper funcion
        if palindrome(str):
            print("This string is palindrome.")
        else:
            print("This string is not palindrome.")
    except:
        print("Invalid input! please enter the valid string.")

# starting point
if __name__ == "__main__":
    main()