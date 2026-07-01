# Write a Python program to print Pascal's Triangle.


def pascal_triangle(n):
    # builds Pascal's triangle
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

def print_triangle(triangle):
    # prints triangle in readable form
    for row in triangle:
        print(" ".join(map(str, row)))

def main():
    try:
        n = int(input("Enter number of rows: "))
        if n <= 0:
            print("Number must be greater than 0")
            return
        triangle = pascal_triangle(n)
        print_triangle(triangle)
    except:
        print("Invalid input!")


# starting point of the program
if __name__ == "__main__":
    main()