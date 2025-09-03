import random

lowest_num = 1
highest_num = 10
answer = random.randint(lowest_num,highest_num)

guesses = 0
is_running = True

print("-----PYTHON RANDOM NUMBER GUESSING GAME-----")
print(f"Select a number between {lowest_num} and {highest_num} ")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("Invalid guess(number out of range)")
            print(f"Please select a number between {lowest_num} and {highest_num} ")
        elif guess < answer:
            print("Too low! Try again")
        elif guess > answer:
            print("Too high! Try again")
        else:
            print(f"Corret!! the answer was {answer}")
            print(f"The number of guess: {guesses}")
            is_running = False

    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num} ")