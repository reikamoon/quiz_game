#Question class has a prompt, and an answer.
class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
    "In the Wizard of Oz, what is the name of Dorothy's dog?\n(a)Fluffy\n(b)Toto\n(c)Caesar\n",
    "What is the capital of California?\n(a)Sacramento\n(b)San Francisco\n(c)Los Angeles\n",
]

answerkey = [
     Question(question_prompts[0], "b"),
     Question(question_prompts[1], "a"),
]

def run_quiz(questions):
     '''Function to run the game'''
     score = 0
     #Initalize with 0 points.
     for question in questions:
         answer = input(question.prompt)
         #For every correct answer, +1 on the score
         if answer == question.answer:
             score += 1
             print("Correct!\n")
     print("You got", score, "out of", len(answerkey), "correct!")

if __name__ == '__main__':
    run_quiz(answerkey)
