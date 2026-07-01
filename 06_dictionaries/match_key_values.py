# Write a Python program to compare two dictionaries and identify matching key-value pairs.


# initializing two dictionaries.
dict_1 = {1: "akram", 2: "ali", 3: "ahmad"}
dict_2 = {4: "hassan", 1: "bilal"}

# function to find matching keys.
def match(dict_1, dict_2):
    for key in dict_1:
        # check if key exists in both dictionaries.
        if key in dict_2:
            print(f"matching key: {key}")

# main function.
def main():
    # call the matching function.
    match(dict_1, dict_2)

# program entry point.
if __name__ == "__main__":
    main()