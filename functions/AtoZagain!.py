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



# n = int(input("Enter a number: "))

# if n > 0:
#     print("Positive")

# if n < 0:
#     print("Negative")

# if n == 0:
#     print("Zero")

# if n % 2 == 0:
#     print("Even")

# if n % 2 != 0:
#     print("Odd")

# # Q2. Student Grade System

# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     print("Grade A+")

# if marks >= 75 and marks < 90:
#     print("Grade A")

# if marks >= 60 and marks < 75:
#     print("Grade B")

# if marks >= 35 and marks < 60:
#     print("Grade C")

# if marks < 35:
#     print("Fail")




# ----------Iterative statements --

# for loop

# s = "dipak"

# for x in s:
#     print(x)

# s = input("Enter any word: ")

# i = 0

# for x in s:
#     print("the chaarter of @",i,"index is:",x)
#     i+=1


# to dispaly the 0 to 10 numbers 

# for x in range(0,11):
#     print(x)


2# to display the 0 t0 20 numbers

# for x in range(0,21):
#     print(x)

#  to display the sum of even  numbers in list

# s = eval(input("Enter the list: "))

# sum = 0

# for x in s:
#     if x % 2 == 0:
#         sum+=x
# else:
#     print("sum of even numbers",sum)



# Q1. Find the sum of all odd numbers from 1 to 100.


# sum = 0
# for x in range(1,101):
#     if x % 2 != 0:
#      sum+=x
       

# print("sum of odd numbers 0 to 100:",sum)


# Q2. Given a list, count how many numbers are positive, negative, and zero.

# l1 = [10,20,-2,0,0,30,50,89,-68]

# positivenum = 0
# negativenum = 0
# zero = 0

# for x in l1:
#    if x >= 0:
#       positivenum+=1
#    if x < 0:
#          negativenum+=1
#    if x == 0:
#       zero+=1
   

# print("positive numbers:",positivenum)
# print("negative numbers:",negativenum)
# print("zero:",zero)
# Q3. Find the largest and second-largest number in a list without using max() or sort().






# Q4. Print the multiplication table of a number from 1 to 20.

# Q5. Given a list, create a new list containing only the numbers that appear more than once.
# l1 = [12,10,10,22,33,12,69]

# counts = {}

# for x in l1:
#    if x in counts:
#       counts[x] +=1
#    else:
#       counts[x] = 1
      


# Q6. Given a list, find the sum of digits of every number and print the total sum of all digits.

# l3 = [10,20,30,40,50,80]

# sum1 = 0

# for i in l3:
#    sum1+=i

# print("total sum of l3",sum1)




# Q7. Check whether each number in a list is a prime number and display the prime numbers.



# Q8. Given a list, remove duplicate elements without using set().

# Q9. Find the second-smallest unique number in a list without using sort() or min().


# Transfer statement---

# while True:
#     n = int(input("Enter jst odd numbers: "))
#     if n % 2==0:
#         break
#     print("Bingo")

# print("Thank you")


# for i in range(2,11):
#     if i == 8:
#         continue
#     print(i)
# print("Thank you")


# for i in range(10):
#     if (i == 7):
       
#         print(i)
#         break

# print("ok its enough..plz break")


# for i in range(1,20):
#     print(i)
#     if (i == 12):
#         print("yup! we found it !")
#         break


# l1 = [10, 20, 30, 40, 50, 60]

# for i in l1:
#     print(i)
#     if(i== 40):
#             print("yup! we found it !")
#             break
        

# Q1.Print each number.
# Stop the loop when you find the first number divisible by both 3 and 5.
# Print "First matching number found!".

# l1 = [12, 7, 18, 25, 30, 9, 40]

# for i in l1:
#     print(i)
#     if (i % 5 == 0 and i % 3 == 0):
#         print("First matching number found!")
#         break
        

# Q2.Check each number in the list.
# Print only the numbers that are not divisible by 3.
# Stop the loop when you encounter the first number divisible by both 5 and 7.
# Print "Loop terminated!" when the loop stops.

# numbers = [15, 22, 9, 18, 35, 42, 27, 50, 60]

# for i in numbers:
#     if (i % 3 != 0):
#         print(i)
#     if (i % 5 == 0 and i % 7 == 0):
#      print("Loop terminated!")
#      break 


# ------continue


# Write a Python program to print numbers from 
# 1 to 20, but skip all numbers divisible by 3 using continue.
# for i in range(1, 21):
#     if (i % 3 == 0):
#         continue
#     print(i)


# Q2.Skip numbers divisible by both 2 and 3.
# Skip numbers less than 10.
# Print all remaining numbers.
# Use continue.

# numbers = [12, 5, 18, 7, 24, 9, 30, 11, 42, 15]



# for num in numbers:
#     if (num % 2 == 0 and num % 3 == 0) or (num < 10):
#         continue
#     print(num)



# Q3.Skip all numbers divisible by 5.
# Add the remaining numbers.
# Print the final sum.
# Use for and continue.

# numbers = [10, 15, 20, 25, 30, 35, 40, 45]

# sum1 = 0
# for i in numbers:
#     if (i % 5 == 0):
#      continue
#     sum+=i
# print("total sum of numbers list",sum1)



# functionn --


# def addition(a,b):
#  s = a + b 
#  return s



# s=addition(23,45)

# print(s)


# write a func ti check given number is even or odd

# def checknum(x):
#     if (x % 2 == 0):
#         print("number is even",x)
#     else:
#         print("number is odd",x)



# checknum(12)

# 2 write a func to find factorial of given numbers ?


# def fac(num):
#     if num < 1:
#         print("not a number")
#     else:
#         factorial = 1
#         i = num
#     while i>1:

#         factorial = factorial * i
#         i-=1

#     print(f"factorial of {i} is {factorial}")



# fac(12)


# Write a function numbers() that prints all numbers from 1 to 10 using a for loop.

def numbers():
    for i in range(1,21):
        print(i)


# Write a function analyze(num) that:
# - Checks whether the number is even or odd.
# - Calculates the sum of its digits.
# - Counts the total number of digits.




# lambda functions-------------------


# Write a lambda function to add two numbers

s = lambda a,b :a+b
# print(s(10,20))


# Write a lambda function to find the square of a number.

a = lambda a: a*a

# print(a(10))
# Write a lambda function to multiply two numbers.

# Write a lambda function to check whether a number is even or odd. 
# Return "Even" or "Odd".

b = lambda n: "even" if n % 2 == 0 else "odd"
# print(b(10))


# Write a lambda function to find the largest of two numbers.

check = lambda n,m: f"{n} is Largest" if n > m else f"{m} is Largest"

# print(check(10,20))


# Write a lambda function that takes three numbers a, b, c and returns:
# - "a is Largest" if a is largest
# - "b is Largest" if b is largest
# - "c is Largest" if c is largest
# - "All are Equal" if all three numbers are equal


def func(a,b,c):
    if a > b and a > c:
        return f"{a}is Largest"
    elif b > a and b > c:
        return f"{b} is Largest"
    elif c > b and c > a:
        return f"{c} is Largest"

    else:
        return "some are equal"


print(func(10,20,30))



check1 = lambda a,b,c: "{a}is Largest" if a > b and a > c else( f"{b} is Largest" if b > a and b > c else f"{c} is Largest" )

print(check1(10,20,30))
        
