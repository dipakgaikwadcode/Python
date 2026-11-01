"""
WAP FOR RECURRSION OF SUM OF FIRST 5 NATURAL NUMBERS
1+2+3+4+5=15

"""

def summ(x):
    if x==5:
        s=5
    else:
       s=x+summ(x+1)
    return s





def factorial(x):
    if x == 1 or x==0:
        f=1
    else:
        f=x*factorial(x-1)
    return f

n=int(input("Enter a number:"))
res=factorial(n)
print(f"factorial of {n} is {res}")