# Write a Python program to unzip a list of tuples into individual lists.


# list of tuples
data = [(1, 2), (3, 4), (5, 6), ("apple", 10), ("banana", 5), ("mango", 8)]

# function to unzip a list of tuples into individual lists.
def main():
    try:
        for item in data:
            print(list(item))
    # handles the unexpected error.
    except TypeError:
        print("Tuples are inconsistent or not iterable properly.")

# main starting point of thr program.
if __name__ == "__main__":
    main()