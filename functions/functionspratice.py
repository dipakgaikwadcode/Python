# 1: Function with no arguments and no return value.

# Question 1 — Easy
# Create a function named student_details() that:
# 1. Prints "My name is Dipak".
# 2. Prints "I am learning Python".
# 3. Prints "My goal is to become a developer".

# def student_details():
#     print("My name is Dipak")
#     print("I am learning Python")
#     print("My goal is to become a developer")


# student_details()


# Q1. Electricity Bill
# Create a function electricity_bill() that calculates the bill for 250 units.
# First 100 units: ₹3 per unit
# Next 100 units: ₹5 per unit
# Remaining units: ₹8 per unit
# Print the total electricity bill.

# def electricity_bill():

#   units = 250 

#   if units <= 100:
#   
#   bill = units * 3
#   elif units >=100:
#      bill = (100*3) 



# Q1. Number Digit Analysis
# Create a function digit_analysis() that stores the number 58342.
# Count the total digits, calculate the sum of digits,
# and print the largest digit in the number.

# def digit_analysis():
#     number = 58342
#     print(len(number))

#     sum = 0
#     for x in number:
      
    

# Q1. Even or Odd
# Create a function even_odd() that stores a number.
# Check whether the number is even or odd and print the result.


# def even_odd():

#   n = int(input("Enter your number buddy: "))

#   if n % 2 == 0:
#     print("Even")
#   else:
#     print("odd")



# even_odd()


# Positive, Negative, or Zero
# Create a function named check_number() that:
# 1. Takes a number from the user.
# 2. Prints "Positive" if it's greater than zero.
# 3. Prints "Negative" if it's less than zero.
# 4. Prints "Zero" if the number is zero.

# def check_number():

#     n = eval(input("Enter your number: "))

#     if n > 0:
#         print("Positive")

#     elif n < 0:
#         print("Negative")
#     else:
#         print("zerooo")


# check_number()



#return multiple values from a function

# def sum_sub(a,b):
#     sum = a+b
#     sub = a-b
#     return sum , sub

# x,y=sum_sub(100,50)

# print("The sum is: ",x)
# print("the subtraction is:",y)


def fact(num):
    result = 1
    while num <= 1:
        result = result*num
        num-=1
        return result

    for i in range(1,5):
        print("the factoorial of :",fact(i))
