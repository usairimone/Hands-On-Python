# Write a Python program to slice a tuple.


tu = (1,2,3,4.232,"usairim",True,5,6,7,8,9)

def main():
    try:
        slice = tu[2:5]
        print(f"The slicing of a tuple is : {slice}")
    # handles the invalid input
    except:
        print("Invalid input! Please enter valid input.")

if __name__ == "__main__":
    # program entry point   
    main()