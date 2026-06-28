# takes integer dataype
n = int(input("Enter a number : "))

# function to get the square of key
def square(n):
    result = {}
    for i in range(1, n + 1):
        result[i] = i ** 2
    print(result)

def main():
    try:
        # prints the key with square values
        show = square(n)
        print(f"The key with their square values are: {show}")
    # handles the invalid input
    except:
        print("Invalid input! Pleas enter the valid input.")

if __name__ == "__main__":
    # starting point of the program
    main()