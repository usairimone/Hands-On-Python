# Write a Python function that takes a number as a parameter and checks whether the number is prime or not.


# function to check number is prime or not.
def prime(num):
    if num < 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            # Found a divisor, so it's not prime
            print(f"{num} is not a prime number.")
            
    return True

def main():
    try:
        num = int(input("Enter the number : "))
        if prime(num):
            print(f"{num} is a prime number.")
    # handles the invalid input,
    except:
        print("Invalid input!")

# starting point of the program.
if __name__ == "__main__":
    main()