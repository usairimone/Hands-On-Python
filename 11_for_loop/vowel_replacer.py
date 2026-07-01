# Write a program that takes a string from the user and uses a for loop to iterate through it. Replace every vowel (A, E, I, O, U, case-insensitive) with an asterisk (*) and print the modified string.Sample Input: "Python Programming"Expected Output: "Pyth*n Pr*gr*mm*ng"


# Function to replace all vowels with '*'
def vowel(str):
    new_str = ""

    # iterate through each character in the input string.
    for ch in str:
        # check if the character is a vowel.
        if ch in "aeiou":
            # replace vowel with '*'.
            new_str += "*"
        else:
            # keep the character uncanged.
            new_str += ch

    # return the modified string.
    return new_str

def main():
    try:
        # take input from the user and convert it to lowercase.
        str = input("Enter the string : ").lower()
        print(vowel(str))
    except:
        # Handle invalid input errors
        print("Invalid input! Please enter the valid input.")

# execute the main function when the script is run directly.
if __name__ == "__main__":
    main()