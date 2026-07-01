# Write a Python program that validates a user's password using boolean expressions.
# The password should satisfy criteria such as:
# Minimum length requirement
# Contains at least one number
# Contains at least one special character
# Any other validation rules you consider necessary


# function to checks the digits and secial characters in password
def validator(password):
    lenght = len(password) >= 10
    special_characters = "!@#$%^&*"
    characters = False
    digits = False
    for ch in password:
        # checks digits in password
        if ch.isdigit():
            digits = True
        # checks charcters of passwords in special_characters
        if ch in special_characters:
            characters = True
    # return if all verified
    return lenght and digits and characters

def main():
    try:
        # takes password  from user
        password = input("Enter a password: ")
        # using helper function
        if validator(password):
            print("Your password is fully based on criteria.")
        else:
            print("Your password is weak and not based on criteria.")
    # handles the invalid input
    except:
        print("Invalid input! PLease enter a valid password.")

if __name__ == "__main__":
    # starting point of program
    main()