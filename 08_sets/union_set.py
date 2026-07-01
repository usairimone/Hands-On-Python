# Write a Python program to create a union of sets.


# first set of elements.
a = {1, 2, 3, 4}

# second set of elements.
b = {3, 4, 5, 6}

def union_sets():
    # union method combines both sets and removes duplicates.
    result1 = a.union(b)

    # | operator also performs union of two sets.
    result2 = a | b

    # using union() method.
    print("Union using union() method:", result1)

    # union using | operator.
    print("Union using | operator:", result2)

def main():
    # call function to perform union operation.
    union_sets()

if __name__ == "__main__":
    # entry point of the program.
    main()