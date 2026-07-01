# Write a program that asks the user for a year and determines whether it is a leap year. A year is a leap year if it is divisible by 4, except for end-of-century years (ending in 00), which must also be divisible by 400.


# function to check whether a give year is leap yar or not
def leap_year(year):
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        return True

def main():
    try:
        # takes year as input
        year = int(input("Enter a year: "))
        # checks whether a year is leap or not.
        if leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    # handles the invalid input.
    except ValueError:
        print("Invalid input. Enter a valid integer year.")

# starting point of the program
if __name__ == "__main__":
    main()

