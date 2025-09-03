import random

options = ("rock", "paper", "scissors")

running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice(Rock, Paper, Scissors): ").lower()
    if player == computer:
        print("It is a tie!")
    elif player =="rock" and computer == "scissors":
        print("You Win!!!")
    elif player=="paper" and computer == "rock":
        print("You Win!!!")
    elif player=="scissors" and computer=="paper":
        print("You Win!!!")
    else:
        print("You loose!")

    if not input("Play again?(Y/N): ").lower() == "y":
      running = False
print()
print("----- THANKS FOR PLAYING -----")
print()