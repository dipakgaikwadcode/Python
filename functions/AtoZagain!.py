# there are 8 types of datatypes

# 1.numeric datatype
# int  im
# float im
# complex im

# 2.string datatype
# str im

# 3.boolean datastype
# bool im


# b = float(a)
# print(type(b))
# print(b)

#indexing /slicing

# name = "dipakgaikwad"


# operators----------


# a = 20
# b = 60

# print((a is b))
# print(id(a))
# print(id(b))



# Write a ternary expression to check:
# - If n is divisible by both 3 and 5 → "FizzBuzz"
# - If divisible by only 3 → "Fizz"
# - If divisible by only 5 → "Buzz"
# - Otherwise → "No Match

n = 45

# print("FizzBuzz")if n % 3 == 0 and n % 5 == 0 else "Fizz" if n % 3 == 0 else "buzz" if n % 5 == 0 else "no Match"


# control flow statement
# conditonal statement

# if--------------------------
# Q1
# if n % 3 == 0 and n % 5 == 0:
#     print("FizzBuzz")
# if n % 3 == 0 and n % 5 != 0:
#     print("Fizz")
# if n % 5 == 0 and n % 3 != 0:
#     print("Buzz")

# # Q2
# If marks are greater than or equal to 90, print "Grade A+"
# If marks are between 75 and 89, print "Grade A"
# If marks are between 60 and 74, print "Grade B"
# If marks are below 60, print "Fail"

# marks = int(input("Enter your marks buddy:"))

# if marks >= 90:
#     print("Grade A+")
# if marks >= 75 and marks <=89:
#     print("Grade A")
# if marks >= 60 and marks <=74:
#     print("Grade B")
# if marks <=60:
#     print("Fail")



# name = input("Enter your Name: ")
# if name == "Harry":
#     print("Hello harry Good night")
#     print("How are you!!!!")


# write a program to check wheather the given number is in bet 1 and 100

# num = int(input("Enter any number: "))

# if num >=1 and num <= 100:
#     print("True number between 1 to 100")
# else:
#     print("False conditionn")



n = int(input("Enter a number: "))

if n > 0:
    print("Positive")

if n < 0:
    print("Negative")

if n == 0:
    print("Zero")

if n % 2 == 0:
    print("Even")

if n % 2 != 0:
    print("Odd")

# Q2. Student Grade System

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A+")

if marks >= 75 and marks < 90:
    print("Grade A")

if marks >= 60 and marks < 75:
    print("Grade B")

if marks >= 35 and marks < 60:
    print("Grade C")

if marks < 35:
    print("Fail")