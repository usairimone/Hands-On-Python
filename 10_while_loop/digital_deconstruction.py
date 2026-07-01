# Problem Statement:Create a script that accepts a single positive integer N from the user. Using a while loop, extract each digit of the number to compute and print the product of all its non-zero digits. Do not convert the integer into a string to process it.Input Example: 2083Output Example: Product of digits: 48 (Calculated as 2 × 8 × 3)



def product_of_digits():
    num = int(input("Enter a positive number: "))

    product = 1

    while num > 0:
        # get last element.
        digit = num % 10
        # removes the last element.
        num = num // 10

        if digit != 0:
            product *= digit

    print(f"Product of digits: {product}")


def main():
    try:
        product_of_digits()
    # handles invalid input.
    except ValueError:
        print("Invalid input! Enter a valid integer.")

# main starting point of the program.
if __name__ == "__main__":
    main()