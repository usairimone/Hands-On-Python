# Write a Python function that checks whether a given list is empty or not using boolean logic.


# checks list is empty or not
def empty(li):
    if li == []:
         return True

def main():
    try:
        # takes input
        input_list = eval(input("Input a list : "))
        if empty(input_list):
                print("The list is empty.")
        else:
            print("The list is not empty.")
    except:
        print("Invalid input. Please enter a valid list.")
        
# starting point of the program
if __name__ == "__main__":
    main()