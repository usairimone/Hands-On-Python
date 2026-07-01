# Write a program that takes an integer N and prints a centered pyramid of asterisks (*) with N rows. The number of stars in each row must follow the odd number sequence (1, 3, 5, ...).


# function to print pyramid.
def print_pyramid(n):
    stars = 1
    for i in range(n):
        spaces = n - i - 1

        print(" " * spaces + "*" * stars)

        # increse star in next row
        stars += 2


def main():
    try:
        n = int(input("Enter rows: "))
        print_pyramid(n)
    # handles the invlaid input.
    except ValueError:
        print("Please enter a valid number.")

# starting point of th program.
if __name__ == "__main__":
    main()