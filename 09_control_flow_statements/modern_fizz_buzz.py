# Loop through numbers from 1 to 50. Print "Fizz" if the number is a multiple of 3, "Buzz" if it is a multiple of 5, and "FizzBuzz" if it is a multiple of both. Otherwise, print the number itself.


# function to find multiples
def fizz_buzz():
    for i in range(1, 51):
        # frist if number is divisible by both 3 and 5, then print otherwise then move to indivisual.
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def main():
    try:
        show = fizz_buzz()
        print(f"{show} is a leap year.")
    # handles the invalid input.
    except:
        print("Invalid input. Loop a valid integer year.")

# starting point of the program
if __name__ == "__main__":
    main()