# take user data and store in list_1.
list_1 = []
for i in range(3):
    list_1.append(input(f"Enter data of first list at index {i} : "))

print("First list is complete. Now enter second list.")

# take user data and store in list_2.
list_2 = []
for i in range(3):
    list_2.append(input(f"Enter data of second at index {i} : "))

# function to find union
def union(list_1, list_2):
    union_list = []
    # checks if element is already in union_list or not.
    for i in list_1:
        if i not in union_list:
            union_list.append(i)
    # checks if element is already in union_list or not.
    for i in list_2:
        if i not in union_list:
            union_list.append(i)
    return union_list

# function to find intersection of two lists
def intersection(list_1, list_2):
    intersection_list = []
    for i in list_1:
        if i in list_2 and i not in intersection_list:
            intersection_list.append(i)
    return intersection_list


def main():
    try:
        # using helper function
        if union(list_1, list_2):
            print(f"The union in both lists are : {union(list_1, list_2)} ")
        # using helper function
        if intersection(list_1, list_2):
            print(f"The intersection in both lists are : {intersection(list_1, list_2)} ")
        else:
            print("There is no union and intersection in both lists.")
    except:
        print("Invalid input! Please enter the valid input.")

if __name__ == "__main__":
    # starting point of the program
    main()