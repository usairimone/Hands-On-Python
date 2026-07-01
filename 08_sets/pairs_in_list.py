# Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.


num = [1,2,3,4,5,6,7,8,9]

target = 10

def elements():
    # store pairs
    pairs = []
    # iterate through by using nested loops for finding target pairs
    for i in range(len(num)):
        for j in range(i + 1, len(num)):

            # check if sum matches to target or not.
            if num[i] + num[j] == target:
                pairs.append((num[i],num[j]))
    # print matching pairs
    print("The pair of sum target are : ", pairs)


def main():
    elements()

# main starting point of the program.
if __name__ == "__main__":
    main()