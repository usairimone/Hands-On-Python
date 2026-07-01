# Build a decimal-to-binary converter. Create a program that requests a base-10 integer N from the user and constructs its raw binary representation using a while loop. You must handle the arithmetic manually by storing reminders in a list or string and updating the original number. Do not use Python's built-in bin() utility.


# function to get the binary of decimal number.
def binary(num):
    # stores binary values.
    bits = []
    while num > 0:
        remainder = num % 2
        bits.append(remainder)
        num = num // 2
    bits.reverse()
    # prints the bits in the form of unlist.
    print(*bits)

def main():
    try:
        num = int(input("Enter the decimal number : "))
        binary(num)
    except:
        # handles the invalid input! Please enter the valid input.
        print("Invalid input! Please enter the valid input.")

# starting point if the program.
if __name__ == "__main__":
    main()