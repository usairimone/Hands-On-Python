# Write a Python program that checks whether a given year is a leap year using boolean logic.


# return leap_year if condition is true
def leap_year(year):
    return (year % 4 == 0)

def main():
    try:
        # takes integer type input
        year = int(input("Enter the year : "))
        # checks leap year using helper function
        if leap_year(year):
            print(f"{year} is leap year.")
        else:
            print(f"{year} is not a leap year.")
    # handles the invalid input
    except:
        print("Invalid input! PLease enter a valid input.")
if __name__ == "__main__":
    # actual point, wher th programs start
    main()