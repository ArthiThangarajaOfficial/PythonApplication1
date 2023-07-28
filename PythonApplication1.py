import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]

while True:

    user_input = input("Type Rock/Paper/Scissors or Q::").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    computer_picks = options[random_number]
    print("Computer picks", computer_picks+".")

    if user_input =="rock" and computer_picks == "scissors":
        print("You Won!")
        user_wins += 1
        continue
    if user_input =="Paper" and computer_picks == "rock":
        print("You Won!")
        user_wins += 1
        continue
    if user_input =="scissors" and computer_picks == "paper":
        print("You Won!")
        user_wins += 1
        continue
    else:
        print("You Lost!")
        computer_wins += 1


print("You Wins",user_wins,"times")
print("Computer Wins",computer_wins,"times")

print("GoodBye!!")



