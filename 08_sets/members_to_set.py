# Write a Python program to add member(s) to a set.


def add_members(s):
    # adding a single element.
    s.add(40)
    # adding multiple elements.
    s.update({50,60})

def main():
    # initial set.
    a = {10, 20, 30}
    print("Original set:", a)
    show = add_members(a)
    print("Updated set:", show)

# main starting point of the program.
if __name__ == "__main__":
    main()