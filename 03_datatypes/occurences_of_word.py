# Write a Python program to count the occurrences of each word in a given sentence.


# function to find the occurrence of each word
def occurences(sentence):
    # store the occurrences of each word in dictionary.
    counts = dict()
    words = sentence.split()
    # using loop to find the occurrences of each word.
    for word in words:
        if word in counts:
            counts[word] +=1
        else:
            counts[word] = 1
    # return dictionary.
    return counts
# prints the occurrence of each word by giving
print(occurences("Write a Python program to count the occurrences of each word in a given sentence."))