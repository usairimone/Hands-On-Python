# Write a Python program to check if a set is a subset of another set.


# main set.
a = {1, 2, 3, 4, 5, 6}
print("The values of a is : ", a)

# possible subset.
b = {2, 3, 4}
print("The values of b is : ", b)

print("Now check if b is a subset of a.")

def check_subset():
    # by using issubset method.
    if b.issubset(a):
        print("Yes, b is a subset of a by using issubset method.")

    # using <= operator.
    if b <= a:
        print("Yes, b is a subset of a by using <= method.")
    
    else:
        print("b is not a subset of a")

def main():
    try:
        check_subset()
    # handles the invlaid input.
    except:
        print("Error Occurred")

# main starting point of the program.
if __name__ == "__main__":
    main()