#operator

a = 10
b = 20
c = 30
d = 50
e = 70
'''
print(a>b)
print(a<b)

print(e>d>c>b>a)



s1 = "python is easy"
s2 = "Python"

print(s1>s2)
'''


#Logical operator

#for boolean behavior
'''
a,b = 10,5                #or operator
c = a>b or b >50
print(c)

'''
'''
a,b = 16,17
rint(c)

'''

#for non-boolean behavior

#string
'''
a = "Python"
b =""
c = a and b
print(c)


a =0
b = 5
c = a or b
print(c)
'''



'''

print(~4)
print(~100)
'''

#logical operator


#bitwise opeartor  & | ^ ~ << >>
'''
a = 10
print(a>>2)
print(a<<2)
'''

 #ternari operator
'''
n1 = 10
n2 = 20
max= a if a>b else b
print(max)


'''

'''
#q1

age = 24

if age > 18:
    print("you have right to vote")
else:
    print("you dont't have right to vote")




#q2


number = 20


if number % 2 == 0:
    print("even number")
else:
  print("odd number")
'''
'''
#q1

age = 20
print("you have right to vote")if age>=18 else print("you dont't have right to vote")



#2
number = 29

print("even")if number %2 == 0 else print("odd")


'''
'''
#max of 3 number   nested ternary
a= 20
b = 10
 c = 40

print(a) if (a > b and a > c) else print(b) if (b > c) else print(c)


'''



#speacial opeartors

#1.identity op ios , is not
'''
n1 = 10
n2 = 10

print("id of n1",id(n1))
print("id of n2",id(n2))
print(n1 is n2)
print(n1 is not n2)

'''  

#2.membership op in not in

s1 = "Python"
s2 = "o"


print(s2 in s1)
print(s2 not in s1)






