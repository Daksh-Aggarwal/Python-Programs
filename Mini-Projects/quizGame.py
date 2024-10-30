print("Welcome to the General Science Quiz!")

play = input("Would you like to participate in the quiz (Y/N)? ")

if play.lower() != 'y':
    quit()

print("Alright! Let's get started.")
score = 0

answer = input("Q1. What is the chemical symbol for water? ")
if answer.lower() == "h20":
    print("You got it right!")
    score += 1
else:
    print("Wrong answer!")

answer = input("Q2. Which planet is known as the \"Red Planet\"? ")
if answer.lower() == "mars":
    print("You got it right!")
    score += 1
else:
    print("Wrong answer!")

answer = input("Q3. What gas do plants absorb from the atmosphere during photosynthesis? ")
if answer.lower() == "carbon dioxide":
    print("You got it right!")
    score += 1
else:
    print("Wrong answer!")

answer = input("Q4. What part of the human body is primarily responsible for filtering waste from the blood? ")
if answer.lower() == "kidneys":
    print("You got it right!")
    score += 1
else:
    print("Wrong answer!")

answer = input("Q5. What is the most abundant gas in Earth's atmosphere? ")
if answer.lower() == "nitrogen":
    print("You got it right!")
    score += 1
else:
    print("Wrong answer!")

print(f"Your total score was {score}/5 ({(score/5) * 100}%).")
print("Thanks for playing the General Science Quiz!")