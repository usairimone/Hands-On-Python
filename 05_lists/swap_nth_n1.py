# list with integer values
li = [0, 1, 2, 3, 4, 5]

def swap(li):
    # store the final swapped result
    new_li = []  

    # step through list in jumps of 2 (pair by pair)
    for i in range(0, len(li), 2):

        # check if second element of the pair exists
        # (important for odd-length lists)
        if i + 1 < len(li):

            # swap the pair: append second first, then first
            new_li.append(li[i + 1])
            new_li.append(li[i])

        else:
            # if no pair exists (last single element), keep it as is
            new_li.append(li[i])

    return new_li

# print the function
print(swap(li))