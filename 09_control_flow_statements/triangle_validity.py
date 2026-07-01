# Problem Statement: Create a program that takes three numerical inputs representing the lengths of three sides of a shape. The program must first determine if these sides can validly form a triangle (the sum of any two sides must be strictly greater than the third side). If it is a valid triangle, classify and print whether it is Equilateral (all sides equal), Isosceles (two sides equal), or Scalene (all sides different). If invalid, print "Invalid Triangle". Concepts Tested: Compound boolean expressions, nesting selection logic, validation principles.Expected Input: 5, 5, 8.


# function to find validity of triangle and type of triangle.
def triangle(x, y, z):
    if ((x + y > z) or (y + z == x) or (x + z == y)):
        print("It is a valid triangle.")
        if x == y == z:
            print("And it's all sides are equal.")
        elif (x == y) or (x == z) or (y == z):
            print("And it is Isoceles triangle.")
        else:
            print("And it's all sides are different.")

def main():
    try:
        # takes input of sides.
        x = int(input("Enter the x side of triangle : "))
        y = int(input("Enter the y side of triangle : "))
        z = int(input("Enter the z side of triangle : "))
        triangle(x,y,z)
    # handles the invalid input.
    except:
        print("Invalid input! Please enter the valid input.")

# starting point of the program.
if __name__=="__main__":
    main()