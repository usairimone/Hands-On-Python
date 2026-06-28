# lenght of input list
lenght_list = int(input("Enter the lenght of list you want to push: "))

# storing the data in list according to lenght of input list
li = []
for i in range(lenght_list) :
    li.append(int(input("Enter a number: ")))

# find the minimum number in a list
def smallest(li):
    return min(li)

def main():
    try:
        # uses helper function
        if smallest(li):
            print(f"The smallest number is {min(li)}")
        else:
            print("PLease enter the digits.")
    # handles the invalid input
    except:
        print("Invalid input! Please enter valid data.")

if __name__ == "__main__":
    # main starting point
    main()