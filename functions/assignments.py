#syntax of function
def wish():
    print("hello")

# wish()

#wrie a function to take a number as input value and print square

# n = int(input("Enter any whole number: "))

def sqaure1(number):
    print("square of number :",number*number)


# c = sqaure1(n)

#write a func to accept the 2 numbers as input and return sum




def summ(a,b):
    return a+b

# d= summ(12,12)

# print("sum of 2 numbers :",d)

#wp func to given value is even or odd

# p = int(input("Enter any whole number: "))

def checkfuc(num):

  if num % 2 == 0:
      print("Even number:",num)
  else:
      print("odd number:",num)

# checkfuc(p)

    
#wp func for finding a factorial 

def findfacto(num):

    factorial = 1

    
    while num >= 1:
           factorial = factorial * num
           num =num-1

    return factorial


# s = findfacto(12)

# print("Factorial og num:",s)


# return multiple values using func


def sumsub(x,y):

 sum = x+y

 sub = x-y 

 return sum, sub

# x,y = sumsub(11,11)

# print("addition og num: ",x)

# print("subtraction og num: ",y)

#-------recurstion----------

# Write a recursive function named count() that:
# 1. Accepts a number as an argument.
# 2. Prints numbers from 10 to 1.
# 3. Uses recursion (not loops).
# 4. Stops when the number reaches 0


# def count(num):

#     count1 = 1

#     while num >=1:
#          print(num)
#          num-=1

#          return count1

# c = count(12)
# print(c)









# p = int(input("Enter any of number: "))

# if p < 0:
#     print("not valid number:")
# else:
#      factorial = 1
#      i = p

#      while i >1:
#          factorial = factorial * i
#          i-=1

#      print("Factorial of num",factorial)


