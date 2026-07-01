# Given a positive integer n, generate its Collatz sequence. The rules for updating the number in each iteration of the loop are:If n is even, the next number is n / 2. If n is odd, the next number is 3n + 1.The sequence always terminates when n becomes 1.Your loop should print each number in the sequence separated by a space and count how many steps it took to reach 1.Constraints: Use floor division (//) to maintain integer values.Test Case:Input: 6Output: Sequence: 6 3 10 5 16 8 4 2 1 | Total steps: 8


def collatz(n):
    steps = 0
    sequence = []

    # Keep iterating until we reach 1
    while n != 1:
        sequence.append(n)  # store current value in sequence

        # Apply Collatz rule:
        if n % 2 == 0:
            n = n // 2      # even case: halve the number
        else:
            n = 3 * n + 1   # odd case: 3n + 1

        steps += 1  # count this transformation

    sequence.append(1)  # include final value

    # Print full sequence and step count
    print("Sequence:", *sequence, "| Total steps:", steps)


def main():
    try:
        # take integer input from user.
        n = int(input("Enter a number: "))

        # guard against invalid domain.
        if n <= 0:
            print("Please enter a positive integer.")
            return

        collatz(n)

    except:
        # Handles invalid input only
        print("Invalid input! Please enter a valid integer.")


# program entry point.
if __name__ == "__main__":
    main()