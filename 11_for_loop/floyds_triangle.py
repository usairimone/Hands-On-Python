# Problem Statement: Write a program that takes an integer N (number of rows) and prints a right-angled triangle filled with sequential numbers starting from 1.


def print_number_triangle(n):

    # start counting from 1.
    start = 1
    # loop for each row.
    for i in range(1, n + 1):
        # loop for numbers in each row.
        for j in range(i):
            # print current number in same line.
            print(start, end=" ")
            # increase number for next print.
            start += 1

        # move to next line after each row.
        print()

def main():
    try:
        # take number of rows from user.
        n = int(input("Enter number of rows: "))
        print_number_triangle(n)

    # handles user invalid input.
    except:
        print("Error Occurred!")


# starting point of the program.
if __name__ == "__main__":
    main()