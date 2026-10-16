#output st

#1 print()

# print("Good aftenoon")
# print()                 #blank print create a new line between that to print stemenents
# print("How are you")



#2 with variable 

# a,b,c = 10,20,30
# print("The values are:",a, b,c, sep=":")    #we can use sep=":"  we want to separate our op with :


#3 end

# print("dipak",end=" ")
# print("gaikwad")

# replacement op {}

name = input("Enter your name:")
age = int(input("Enter your age:"))
salary = input("Enter your salary:")


print(name,"is earning Rs.",salary,"and his age is",age)
print("{} is earning Rs.{} and his age is {}".format(name,salary,age))
print(f"{name} is earning Rs.{salary} and his age is:{age}")