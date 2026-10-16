#if
#if-else
#if-elif-else

#.---------------------------if--------------------------------------

# n = int(input("Enter number above 15:"))
# if n<15:
#     print("entered  number is less than 15!")
# print("n:",n)

# Q1 accept two number and print max of 2 number

# num1 = int(input("Enter the number 1:"))
# num2 = int(input("Enter the number 1:"))

# max_num = num1
# if num2>num1:
#     max_num = num2
# print("Maximum number is:",max_num)


# Q2  accept a number and print its absolute value

# number3 = float(input("Enter the number:"))

# if number3 


#Q3 Write a Python program using only an if statement to check whether the number is greater than 10.

# number = int(input("Enter a number:"))

# if number >10:
#     print("Number is greater than 10")
#     print(number)


# Q4. Write a Python program that prints "Number is not divisible by 2 and 3 both" if the number is not divisible by both 2 and 3.
# If the number is divisible by both 2 and 3, print nothing.

# num = int(input("Enter the whole number:"))

# if (num %2 == 0  and  num % 3 == 0):
#     print("number is not divisible both")


# Q5.Write a Python program that takes an integer as input and prints "Valid Number" only if all these conditions are satisfied:
# - The number is between 100 and 999.
# - The number is even.
# - The number is NOT divisible by 5.
# - The number is divisible by 3 OR 7.


# number1 = int(input("Enter any number: "))

# if (number1 (100,999) or number1 >=0 or number1 * 5 !=0 and number1 % 3 ==0 and number1 % 7 == 0):
#     print("valid number:")







#if-else---------------------------------

# n1 = int(input("Enter your num1:"))
# n2= int(input("Enter your num2:"))

# if n1>n2:
#     print("n1 is max")
# else:
#     print("n2 is max")

# Q1 aacept the number and print whether it is evn or odd

# number5 = int(input("Enter your number:"))

# if number5 % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")


# Q2  accept the number is positive or naegative

# number6 = int(input("Enter the number:"))

# if number6 >= 0:
#     print("number is positive")
# else:
#     print("number is negative")



#ifelifeif----------------------------------------


#accept marks of 5 subject and print precentage and class obtained 

sub1 = int(input("Enter sub1 marks: "))
sub2 = int(input("Enter sub2 marks: "))
sub3 = int(input("Enter sub3 marks: "))
sub4 = int(input("Enter sub4 marks: "))
sub5 = int(input("Enter sub5 marks: "))

total = (sub1+sub2+sub3+sub4+sub5)

percentage = (total / 500) * 100

print("percentage:", percentage)


if percentage >= 75:
    print("Ditinction")
elif percentage >= 60 and percentage < 75:
    print("first")
elif percentage >= 50 and percentage < 60:
    print("Second")
elif percentage >= 40 and percentage < 50:
    print("pass")
else:
    print("invalid marks")


