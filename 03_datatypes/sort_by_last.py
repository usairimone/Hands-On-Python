# initialize list
li = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# function to sort the tuples in a list
def sort():
    return sorted(li, key = lambda item : item[1])
# prints sort by last element.
print(sort())