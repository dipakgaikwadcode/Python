
from random import *

# 1.random()   between o to 1

# x = random()
# print(x)

# for i in range(3):
#     print(random())


#2.randint(n1,n2)

# x = randint(1,20)
# print(x)


#3.uniform(n1,n2)        gives us decimal values

# for i in range(3):

#  print(uniform(100,200))

#4.randrange()

# for i in range(3):
#     print(randrange(1,10,2))


# #5.choice(), choices(), sample()

l1 = [10,20,"python", "java","ds",45,70]
# print(choice(l1))     #choice
# print(choices(l1,k=2))  


# sample()

# s = "abcdefghdkslefd"

# print(sample(s,5))



# #6.shuffle()

# l2 = [10,20,"python", "java","ds",45,70]
# print(l2)

# shuffle(l2)
# print("after shuffle",l2)


# #7.triangular()

# for i in range(3):
#    print(triangular(10,100,2))


# 6 digit otp


# x = randint(1111,9999)
# print( "the otp is",x)

import random
import string

def randomstring(strlength = 10):
    letters = string.ascii_lowercase
    print(letters)
    l=[choice(letters) for x in range(10)]
    print(l)
    s = join(l)
    print(s)


randomstring()