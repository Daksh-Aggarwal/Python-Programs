import random as rm

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Choose Rock/Paper/Scissors or enter 'Q' to quit. ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        print("Invalid input!")
        continue

    random_number = rm.randint(1, 3)
    # 1 = Rock, 2 = Paper, 3 = Scissors
    computer_input = options[random_number - 1]

    print(f"The computer chose {computer_input}.")

    if (user_input == "rock" and computer_input == "scissors") or (user_input == "scissors" and computer_input == "paper") or (user_input == "paper" and computer_input == "rock"):
        print("You won!")
        user_wins += 1
    elif user_input == computer_input:
        print("Tie!")
    else:
        print("You lost!")
        computer_wins += 1

print(f"You won {user_wins} times.")
print(f"The computer won {computer_wins} times.")
print("Thanks for playing!")