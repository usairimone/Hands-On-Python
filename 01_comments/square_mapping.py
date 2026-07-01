# Write a Python script to generate and print a dictionary that contains numbers between 1 and n in the form:
# (x, x * x)


# take integer input.
n = int(input("Enter a number : "))

# create dictionary of squares.
def square(n):
    result = {}
    # store number and its square.
    for i in range(1, n + 1):
        result[i] = i ** 2
    # display dictionary.
    print(result)

def main():
    try:
        # call square function.
        show = square(n)
        # print returned value.
        print(f"The key with their square values are: {show}")
    # handle invalid input.
    except:
        print("Invalid input! Pleas enter the valid input.")

if __name__ == "__main__":
    # start program execution.
    main()