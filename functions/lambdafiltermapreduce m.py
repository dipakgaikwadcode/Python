#reduce()
from functools import *
l1=[10,20,30,40]
res=reduce(lambda x,y:x+y,l1)
print("res:",res)

#product of all numbers from 1 to 10
res=reduce(lambda x,y:x*y,range(1,11))
print("res:",res)



#map()

# l1=[1,2,3,4]
# l2=[10,20,30,40]
# res=list(map(lambda x,y:x*y,l1,l2))
# print(res)


#using normal function
# def doublen(x):
#     return 2*x
# l1=[1,2,3,4]
#
# res=list(map(doublen,l1))
# print(res)

#using lambda function
# l1=[1,2,3,4]
# res=list(map(lambda x:2*x,l1))
# print(res)

#Filter
#


#a.normal function

# def isEven(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
# l1=[10,9,8,5,14,18]
#
# res=list(filter(isEven,l1))
# print(res)

#b.using lambda
# l1=[10,9,8,5,14,18]
# res=list(filter(lambda x:x%2==0,l1))
# print(res)



#lambda

#minimium of 2 numbers
# s=lambda x,y: x if x<y else y
# print("Min=",s(25,10))

#sum of 2 numbers

# s=lambda x,y:x+y
# print("Addition:",s(10,20))

#square of a number using lambda

# s=lambda x:x*x
# print("Sqaure of number: ",s(4))