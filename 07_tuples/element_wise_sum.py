# Write a Python program to compute the element-wise sum of given tuples.


# tuples with same lenght
x = (1, 2, 3, 4)
y = (3, 5, 2, 1)
z = (2, 2, 3, 1)

# function to sum corresponding elements
def element_sum():
    print(x)
    print(y)
    print(z)
    # using zip function to sum based on their positions
    add = tuple(map(sum, zip(x,y,z)))
    return add

def main():
    try:
        show = element_sum()
        print(f"The element-wise sum of given tuples is : {show}")
    # handles the unexpected error
    except:
        print("Invalid input! Please enter the valid input.")

# main starting point of the program.
if __name__ == "__main__":
    main()