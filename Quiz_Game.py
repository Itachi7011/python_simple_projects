import random

# Define a dictionary of questions and answers
questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the smallest country in the world?": "Vatican City",
    "What is the largest living species of lizard?": "Komodo Dragon",
    "What is the deepest ocean?": "Pacific Ocean"
}

# Initialize score to 0
score = 0

# Define a function to ask a question
def ask_question(question, answer):
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("Correct!")
        return 1
    else:
        print("Incorrect. The correct answer is " + answer)
        return 0

# Ask a series of random questions
for _ in range(5):
    question, answer = random.choice(list(questions.items()))
    score += ask_question(question, answer)
    del questions[question]  # Remove the question from the dictionary

# Print the final score
print("Your final score is " + str(score) + " out of 5")