# Create a game where the program picks a secret number (e.g., 42). The user has exactly 5 attempts to guess it. Prompt the user for a guess inside a while loop. If the guess is too high, print "Too high!". If it is too low, print "Too low!". If they guess correctly, terminate the loop and congratulate them. If they run out of attempts, print "Game Over!"

# target number
secret_number = 42

# total attempts
attempts = 5

# while loops iterate until the condition is true.
while attempts > 0:
    guess = int(input("Enter your guess: "))
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Correct! You win!")
        break
    # it minuc the attempts every time you guess the number.
    attempts -= 1

# prints if user loose to guess the number in all attempts.
if attempts == 0 and guess != secret_number:
    print("Game Over!")