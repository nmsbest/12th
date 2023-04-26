# Write a py prog that creates a gk quiz consisting of any 5 questions of your choice the questions should be displayed randomly . create a user defined function score of the quiz and another user defined function remark (score value) that accepts final score to display remak as follows
# Credits: Dhruv , XII-D

import random

# Define a list of questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Mars", "Jupiter", "Venus", "Saturn"],
        "answer": "Jupiter"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Yen", "Dollar", "Euro", "Pound"],
        "answer": "Yen"
    },
    {
        "question": "Who invented the telephone?",
        "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Guglielmo Marconi"],
        "answer": "Alexander Graham Bell"
    },
    {
        "question": "What is the tallest mammal in the world?",
        "options": ["Giraffe", "Elephant", "Hippopotamus", "Rhino"],
        "answer": "Giraffe"
    }
]

# Define a function to display a random question
def display_question():
    question = random.choice(questions)
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    answer = input("Enter your answer (1-4): ")
    if answer.isdigit() and int(answer) in range(1, 5):
        if question["options"][int(answer)-1] == question["answer"]:
            return 1
    return 0

# Define a function to calculate the score
def calculate_score():
    score = 0
    for i in range(5):
        print(f"Question {i+1}:")
        score += display_question()
        print()
    return score

# Define a function to display a remark based on the final score
def display_remark(score):
    if score == 5:
        print("outstanding")
    elif score >= 3:
        print("Good")
    elif score >= 1:
        print("need to take interset")
    else:
        print("gk will always help ypou take interest")

# Call the functions to run the quiz
print("Welcome to the GK Quiz!")
print("Answer the following 5 questions:")
print()
score = calculate_score()
print()
print(f"Your final score is {score}/5.")
display_remark(score)