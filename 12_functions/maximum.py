# Write a Python function to find the maximum of three numbers.


# function to find the maximum from 3 numbers.
def maximum(a,b,c):
    result = max(a,b,c)
    return result

def main():
    try:
        # takes three integer values from user.
        a = int(input("Enter the value of a : "))
        b = int(input("Enter the value of b : "))
        c = int(input("Enter the value of c : "))
        show = maximum(a,b,c)
        print(f"{show} is the maximum from all three numbers.")
    # handles the invalid input.
    except:
        print("Invalid input!")

# starting point of the program.
if __name__ == "__main__":
    main()