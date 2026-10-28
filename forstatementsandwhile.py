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

"""
1.Print number from 1 to 10 








2.Accept a number and print its table
3.Accept name from user until you enter your name
4.Accept a number and print reverse of that number   n 236   o/p 632

"""





#while loop 

# Q1. Print numbers in reverse
# Print numbers from 20 down to 1.


# i = 20

# while i >= 1:
#   print(i)
#   i-=1


# #Q2. Sum of digits
# num = int(input("Enter the number:"))

# i = 0
# total = 0

# while i <len(num):
#   total +=int(num[i])
#   i+=1


#   print(total)


  #print numbers from 1 to 100

# i = 1
# while i <= 100:
#  print(i)
#  i+=1


 #2.print numbers from 100 to 1

# i = 100

# while i>=1:
#  print(i)
#  i-=1

#3.print the multiplication table of a number n

# n = int(input("Enter a number: "))

# i = 1

# while i <= 10:
#     print( n*i )
#     i+=1


#4. print the element of the following list using loop

# b = [1,4,6,8,9,5,4,46,66,77,88,55]

# i = 0

# while i < len(b):
#     print(b[i])
#     i+=1




# idx = 0
# while idx < len(b):
#     print(b[idx])
#     idx+=1
 

#5.search for a number x in this tuple using loop


b = [1,4,6,8,9,5,4,46,66,77,88,55]

# x = 77
# i = 0
# while i < len(b):


#     if(b[i] == x ):
#      print("value fonud at indx", i)
#     i+=1


#for looppppppppppppppppppppppppppppp
# x = 77

# for i in range(len(b)):

#  if(b[i] == x ):
#    print("value fonud at indx", i)
#    i+=1
  
# Find all the numbers that appear more than once and print each repeated number only once.
# numbers = [2, 4, 6, 2, 8, 4, 10, 6, 12]


# new_list =[]

# for i in (numbers):

#  if numbers.count(i) > 1 and i not in new_list:

#   new_list.append(i)

#   print(new_list)
  


# i = 0

# while i < len(numbers):

#  if numbers.count(numbers[i]) > 1 and i not in new_list:


#   new_list.append(i)
#   i+=1

#   print(new_list)