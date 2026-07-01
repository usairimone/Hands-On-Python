# A local theater charges different ticket prices based on a customer's age. Write a program that reads an integer age and calculates the ticket cost according to these rules:


# function to verify age.
def age_verification(age):
    if age < 5:
        print("Ticket is free for you !")
    elif age <= 17:
        print("Rs.1000 for tciket")
    elif age <= 64:
        print("Rs.1500 for tciket")
    else:
        print("Rs.700 for tciket")

def main():
    try:
        age = int(input("Enter the age : "))
        age_verification(age)
    # handles the invalid age.
    except:
         print("Invalid input. Enter a valid age.")

# starting point of the program
if __name__ == "__main__":
    main()