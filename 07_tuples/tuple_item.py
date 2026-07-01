# Write a Python program to create a tuple of numbers and print one item.


# takes input as a list.
numbers = int(input("Enter the lenght of numbers : "))

# store the numbers in list.
li = []
for i in range(1, numbers +1):
    li.append(i)
print(li)

# types casting list into tuples.
tu = tuple(li)

# function to get item from tuple.
def item(tu):
    return tu[2-1]

def main():
    try:
        show = item(tu)
        print(f"The item of a tuple is : {show}")
    # handles the invalid input.
    except:
        print("Invalid input! Please enter valid input.")

if __name__ == "__main__":
    # starting point of the program.
    main()