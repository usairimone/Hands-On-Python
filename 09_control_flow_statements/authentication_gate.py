# Problem Statement: Write a login verification system. The system has a hardcoded default username ("admin") and password ("secure123"). The program should first request a username. If the username is incorrect, print "User not found" and terminate. If correct, it should prompt for the password. If the password is correct, display "Access Granted"; otherwise, display "Access Denied".


# function for verification system.
def login(user_name):
    if user_name == "admin":
        # if user name will correct then it will ask for password.
        password = input("Enter the password: ")
        if password == "secure123":
            print("Access Granted.")
        else:
            print("Access Denied.")
    else:
        print("User not found.")

def main():
    try:
        user_name = input("Enter the user name: ")
        login(user_name)
    # handles the invalid input.
    except:
        print("Invalid input! Enter the valid input.")

# starting point of the program
if __name__ == "__main__":
    main()