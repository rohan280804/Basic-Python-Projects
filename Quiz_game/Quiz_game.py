questions = ("How many elements are in the periodic table: ",
             "Which Animal lays the largest egg: ",
             "What is the most abundant gas in Earth's atmosphere: ",
             "How many bones are in the human body: ",
             "Which planet is the hottest in the solar system: ")
options = (("A.","B.","C.","D."),
           ("A.","B.","C.","D."),
           ("A.","B.","C.","D."),
           ("A.","B.","C.","D."),
           ("A.","B.","C.","D."))
answers = ("C","D","A","A","B")
guesses = []
score = 0
question_number = 0

for question in questions:
    print("-------------------")
    print(question)
    for option in options[question_number]:
        print(option)

    guess = input("Enter A, B, C, D : ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("Correct!!")
    else:
        print("Incorrect!!")
        print(f"{answers[question_number]} is the correct option")
    question_number += 1

print("-------------------")
print("RESULTS")
print("-------------------")

print("answers: ",end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ",end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is {score}%") 