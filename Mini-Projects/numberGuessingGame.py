import random as rm

print("Welcome to the Number Guessing Game!")

play = input("Would you like to play the game (Y/N)? ")

if play.lower() != 'y':
    quit()

print("Alright! Let's get started.")

while True:
    max_range = input("Enter the higher end of the range: ")

    if max_range.isdigit():
        max_range = int(max_range)
        break

    else:
        print("Please enter a number.")
        continue

random_number = rm.randint(1, max_range)
guesses = 0

print(f"Guess the number lying between 0 and {max_range + 1}.")

while True:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
    else:
        print("Please enter a number.")
        continue

    if guess == random_number:
        break
    elif guess < random_number:
            print("Your guess was lower than the random number!")
    else:
        print("Your guess was higher than the random number!")

print(f"Congratulations! You got it right in {guesses} guess(es).")