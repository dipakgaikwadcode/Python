#Special op
#2.membership op in not in

l1=[10,20,"Python"]
print("Java" not in l1)

"""
s1="Python"
s2="o"
print(s2 in s1)
print(s2 not in s1)
"""


#1.identity op  ios ,is not

'''
n1=[10,20,30]
n2=[10,20,30]
#n1=10
#n2=10
print("id of n1=",id(n1))
print("id of n2=",id(n2))
print(n1 is n2)
print(n1 is not n2)

'''


#Ternary operator

#max of 3 numbers
"""
a,b,c=20,10,50
print("a is max") if a>b and a>c else print("b is max") if b>c else print("c is max")
"""

"""
Q1.Assign age to variable and display wheher he is eligible for voting or not
"""
'''
age=12
print("Eligble")if age>=18 else print("Not Eligible")
'''

"""
Q2.Assign a number to a variable and display whether it is even or odd

"""

"""
a=12
print("Even")if a%2==0 else print("Odd")
"""


'''
a,b=100,20
print("a is max")if a>b else print("b is max")
'''


'''
a,b=100,20
max= a if a>b else b
print("Max=",max)
'''



#bitwise operator   & | ^ ~ << >>

'''
a=10
#print(a<<2)
print(a>>2)
'''

'''
print(~4)
print(~101)
print(~False)

'''

"""
a=4
b=5 
print(a&b)
print(a|b)
"""




#Logical operator


#for non-boolean behavior

'''
a="Python"
b=""
c=b or a
print(c)
'''


'''

a=0
b=5
c=a or b
print(c)
'''



#for boolean behavior

'''
a,b=10,5
c=not(a<b)
print(c)
'''

'''
a,b=10,5
c=a<b or b>50
print(c)
'''
'''
a,b=10,5
c=a<b and b<50
print(c)
'''


#Relational op with string

'''
s1="python is easy"
s2="python"
print(s1>s2)
'''
