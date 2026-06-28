# Return even if condition is true
def even(number):
    return (number % 2 == 0)

def main():
    try:
        # taking integer
        number = int(input("Enter a number: "))
        # check parity using helper function
        if even(number):
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")
    # handling in valid input
    except:
        print("Invalid input! Please enter a valid input.")

if __name__ == "__main__":
    # entry point
    main()