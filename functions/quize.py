


# print("Q1.Which data type is immutable in Python?")
# print("A. List")
# print("B. Dictionary")
# print("C.Set")
# print("D.Tuple")

# Q1 = input("Enter answe:")

# if Q1 == "B" or Q1 == "Tuple" or Q1 == "tuple":
#     print("correct ans buddy!")
#     score+=1
# else:
#     print("wrong ans:")

# print("\nQ2. Which keyword is used to define a function in Python?")
# print("A. function")
# print("B. def")
# print("C. fun")

# print("D. define")
# # print("Answer: B. def")
# Q2 = input("Enter answe:")

# if Q2 == "B" or Q2 == "def":
#     print("correct ans buddy!")
#     score+=1
# else:
#     print("wrong ans:")

# print("score",score)


# def quize(question, a,b,c,d,correctans):

#  print("question")
#  print("a")
#  print("b")
#  print("c")
#  print("d")

#  answer = input("Enter ans:")

# if "answer" == "correctans":
#   print("correct ans buddy !")

# score = score + 1

# else:
                         


# Simple Quiz Game using lists

questions = [
    "What is the capital of India?",
    "Which language is used to write this program?",
    "What is 12 x 3?",
    "Which planet is known as the Red Planet?",
    "Which data type is used to store multiple items in one variable?",
]

options = [
    ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
    ["A. Java", "B. C++", "C. Python", "D. Ruby"],
    ["A. 36", "B. 33", "C. 39", "D. 42"],
    ["A. Venus", "B. Jupiter", "C. Saturn", "D. Mars"],
    ["A. int", "B. list", "C. float", "D. bool"],
]

answers = ["B", "C", "A", "D", "B"]

score = 0

print("===== Welcome to the Quiz =====\n")

for i in range(len(questions)):
    print(f"Q{i + 1}. {questions[i]}")
    for option in options[i]:
        print("   ", option)

    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == answers[i]:
        score += 1   # right answer = +1
        print("Correct! +1 point")
    else:
        score += 0   # wrong answer = 0
        print(f"Wrong! +0 points. The correct answer is {answers[i]}.")

    print(f"Current score: {score}\n")

print("===== Quiz Over =====")
print(f"Your score: {score} out of {len(questions)}")

percentage = (score / len(questions)) * 100
if percentage == 100:
    print("Excellent!")
elif percentage >= 60:
    print("Good job!")
else:
    print("Keep practicing!")