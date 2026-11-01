#write a program for recursion

# def factorial(x):
#    if x == 1 or x == 0:
#       f=1

#    else:
#       f=x*factorial(x-1)

#    return f

# n = int(input("Enter any num: "))
# res = factorial(n)
# print(f"factorial of {n} is {res}")


#wap for recursion of sum of  first 5 natural numbers 
  
# def countsum(x):

#     if x == 5:

#       s= 5
    

#     else:
#        s = x+countsum(x+1)

#     return s






# n = int(input("Enter your nnum: "))





#-------------------------------------lambda/filter/map/reduce --------------------------------------------------------

#reduce
#find sum of l1 using lambda
# from functools import *
# l1 =[10,20,30,40]
# res = reduce(lambda x, y: x+y,l1)
# print("sum of l1:", res)

#product of all numbers form 1 to 10

from functools import *
res = reduce(lambda x,y:x*y, range(1,11))

print(res)





#mappp()
 #normal functioon 
# def doublen(x):
#     return 2* x
# l1 = [1,2,3,4]

# res = list(map(doublen,l1))

# print(res)

#using lambda

# l1 = [1,2,3,4]
# result = list(map(lambda x:x*2 ,l1))
# print(result)

#using lambda   
# l1 = [1,2,3,4]
# l2 = [1,2,3,4]

# result = list(map(lambda x,y:x*y, l1,l2))

# print(result)


#---------Filter()
 #using normal function
# def isEven():
#     if x % 2 == 0:
#         return True
#     else:
#         return False

# l1 = [10,9,8,5,14,18]

# res=list(filter(isEven,l1))


#using lambda


# l1 = [10,9,8,5,14,18]

# res=list(filter(lambda x:x%2 == 0,l1))

# print(l1)



# inp_list = ['t','u','t','o','r','i','a','l']

# res = list(filter(lambda x:x!='t',inp_list))

# print(res)
# s = lambda x:x*x
# print("Square of number:", s(4))


# d = lambda x,y:x+y
# print("Sum of number:", d(4,5))

#Q2.minium of 2 number

# d = lambda x,y :x if x<y else y
# print("mimnum:", d(4,5))



# list_1 =[5,10,20,30,40,'a','x',50]
# list_2 =[10,40,'a']

# list_3 =list(filter(lambda x: x not in list_2 , list_1))