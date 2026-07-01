# Problem Statement:Write a program that continuously prompts the user to enter a number. The program should maintain a running sum of all numbers entered. If the user enters a negative number, the program must immediately print the total sum (excluding the negative number) and terminate the loop. 


# function to add numbers till user gice positive integers
def add():
    total = 0
    while True:
        num = int(input("Enter the positive number: "))
        if num < 0:
            break
        total += num

    print(f"The sum of all number is : {total}")
    
def main():
    try:
        add()
    # handles the invalid input.
    except:
        print("Invalid input! Please enter the valid input.")

# starting point of the program.
if __name__ == "__main__":
    main()