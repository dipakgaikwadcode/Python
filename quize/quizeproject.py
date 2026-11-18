quiz = [
    {
        "Question":"Q1.Which data type is immutable in Python?",
        "Options":["List", "Dictionary", "set", "Tuple"],
         "Answer":"Tuple"
         
     },
     {
        "Question": "Q2.Which keyword defines a function?",
        "Options": ["function", "def", "return", "print"],
        "Answer": "def"
    }
     ]

score = 0

for q in quiz:
  print(q["Question"])
  print(q["Options"])
  user_ans =(input("Enter your Ans:"))

  if user_ans == q["Answer"]:
    score+=1

