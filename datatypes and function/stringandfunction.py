# s = "python is easy to learn"
# x =s.count('a',14,24)
# x =s.count('Java')
# print(x)



#replace 

s1 = "dipak gaikwad"
s1 = s1.replace("dipak","shubham")

print(s1)


#split()

s = "22-10-2026"
li=s.split("-")
print(li)





#9)join()

s = "python is easy"
s1="-".join(s)
print(s1)




#10) changing cases upper , lower, swapcase , title , capitalizeee

s1="Python is EAsy "
# s2=s1.upper()
# s2=s1.lower()
# s2=s1.swapcase()
# s2=s1.title()
s2=s1.capitalize()
print(s2)



#startwith()  endwith()

s = "python is easy to learn"
print(s.startswith("py"))




#write a program to aceept some string from the keyboard and display its 
# characters by negative index wise

s = input("Enter any string: ")

i=0

for x in s:
    print("The positive index of string{} and at negative index{}iis {}")