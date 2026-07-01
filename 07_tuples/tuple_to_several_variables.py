# Write a Python program to unpack a tuple into several variables.


# tuple with different datatpes.
tu = (42, "Python", 3.14, True, [1, 2, 3])

def main():
    try:
        # unpack tuple into several variables
        a, b, c, d, e = tu
        # prints varaibles
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)
    # handles the invalid input.
    except:
        print("Tuple size does not match variables.")

# program entry point
if __name__ == "__main__":
    main()