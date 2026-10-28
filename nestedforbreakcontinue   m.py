"""for i in range(5):
    for j in range(4):
        print("Hello ",end="")
    print()
    """

"""for i in range(1,4):
    print("* " * i)
"""

#break
"""
i=1
while i<5:
    print("Hello")
    i+=1
    #break
    continue
    print("Hi")
print("bye")
"""
"""
1 2 3 4 6 7 8 9 10 (use only 1 while loop)
Accept a number and print whether it is prime number or not
"""


n=int(input("Enter a number: "))
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break

if flag==1:
    print("Not prime number")
else:
    print("Prime number")


