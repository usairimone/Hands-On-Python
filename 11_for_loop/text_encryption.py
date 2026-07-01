# Create a basic text encryption loop. Take a lowercase string and a shift integer N. Use a for loop to shift each letter forward in the alphabet by N positions. Wrap around to the letter 'a' if the shift goes past 'z'. Keep spaces unchanged.


# this function shifts each letter by a given number.
def encrypt_text(text, shift):
    result = ""

    # go through each character one by one.
    for ch in text:

        # if character is space, keep it as it is
        if ch == " ":
            result += " "
        else:
            # convert letter to number.
            old_index = ord(ch) - ord('a')

            # shift the number.
            new_index = (old_index + shift) % 26

            # convert number back to letter.
            result += chr(new_index + ord('a'))

    # return final encrypted text.
    return result


def main():
    try:
        # take input from user.
        text = input("Enter lowercase text: ")
        shift = int(input("Enter shift value: "))

        # check if text is only lowercase.
        if not text.islower():
            raise ValueError("Text must be lowercase only")

        # call encryption function.
        encrypted_text = encrypt_text(text, shift)

        print("Encrypted text:", encrypted_text)

    except:
        # Handle any unexpected errors
        print("Unexpected error:")


# starting point of the
if __name__ == "__main__":
    main()