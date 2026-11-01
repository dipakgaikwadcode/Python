"""

str="Python"
i=0
l=len(str)  #6
for x in str:
    print(x,"positive index:",i,"negative index:",i-l)
    i=i+1

"""

"""
i=0
while i<5:
    print("Hello")
    i=i+1
"""

# 1.Print number from 1 to 10 
 
# for i in range(1, 11):
#  print(i)




# 2.Accept a number and print its table


# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{num} X {i} = {num * i}")

# 3.Accept name from user until you enter your name



# for i in range(100):
#     name = input("Enter your name: ")

#     if name == "Dipak":
#         print("Name matched!")
#         break

# 4.Accept a number and print reverse of that number   n 236   o/p 632


#5. display odd numbers from 0 to 20


# Q1. Medium — Count positive and negative numbers
# Given a list, count how many numbers are positive, negative, and zero.

# numbers = [10, -5, 0, 25, -12, 8, 0, -3]

# positive = 0
# negative = 0
# zero = 0


# for i in numbers:

#     if i > 0:
#         positive+=1
#     elif i < 0:
#         negative+=1
#     else:
#         zero+=1


# print("Positive numbers:", positive)
# print("Negative numbers:", negative)
# print("Zeros:", zero)



# Q2. Hard — Find the second-largest number
# Find the second-largest distinct number without using sort(), max(), or min()


# Q1. Sum of even and odd numbers
# Given a list, calculate the sum of all even numbers and the sum of all odd numbers separately.

# numbers = [12, 7, 18, 5, 21, 30, 9, 14]


# even = 0
# odd = 0

# for i in numbers:

#  if i % 2 == 0:
#         even+=i
#  else:
#     odd+=i


#     print("count of even numbers:", even)
#     print("count of odd numbers:", odd)



# Q2. Count vowels
# Count how many vowels are present in the string.

# text = "python programming is interesting"


# vowels = 0

# for i in text:

#  if i in "aeiou":
#    vowels+=1

# print("count of vowels :",vowels)


# Q3. Find the largest number
# Find the largest number in the list without using max() or sort().


# numbers = [45, 12, 89, 34, 67, 23]


# maxnum = numbers[0]

# for i in numbers:

#  if i > maxnum:
#    maxnum = i

# print("Largest number:",maxnum)


# Q4. Calculate the factorial
# Calculate the factorial of 6 using a for loop.


#Q5 Reverse the list using a for loop without using reverse() or slicing ([::-1]).

numbers = [10, 20, 30, 40, 50]

# reversed_list=[]


# for i in range(len(numbers)-1,-1,-1):
#     reversed_list.append(numbers[i])


# print(reversed_list)


# for i in reversed(numbers):
#     print(i,end="")





# s = "dipakgaikwad"

# for i in s:
#     print(i)


# Q1. Sum of Even Numbers
# Write a program to find the sum of all even numbers between 1 and 50.


# summ =0

# for i in range(1,51):

#     if i % 2 ==0:
#         summ+=i


# print("Sum of even numbers:",summ)


# Q2. Multiplication Table
# Accept a number from the user and print its multiplication table from 1 to 10.


n = int(input("Enter your any number: "))

for i in range(1,11):

 result = n * i

 print(f"{n} X {i} = {result}")

