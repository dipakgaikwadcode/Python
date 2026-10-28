#12.isalnum(),isalpha,isdigit(),islower()

# s="  "
# print(s.isalnum())
# #print(s.isalpha())
# #print(s.isdigit())
# #print((s.islower()))
# #print(s.istitle())
# print(s.isspace())


#11.startswith() endswith()

"""
s="Python is easy to learn"
#print(s.startswith('Py'))
print(s.endswith('n'))
"""



#10.Changing cases upper,lower,swapcase,title,capitalize

#s1="Python IS EaSY"
#s2=s1.upper()
#s2=s1.lower()
#s2=s1.swapcase()
#s2=s1.title()
# s2=s1.capitalize()
# print(s2)


#9.join()

s="Python is easy"
l1=["Python","is","easy"]
s1=" ".join(l1)
print(s1)


#8.split() 

# s="22-10-2026"
# l1=s.split("-")
# print(l1)


"""
s="Python is easy to learn"
l1=s.split()
print(l1)
"""


#7.replace()
"""
s1="Python is easy to use"
s1=s1.replace("Python","Java")
print(s1)
"""




#6.count()

# s="Python is easy to learn"
# #x=s.count('a',14,24)
# x=s.count('Java')
# print(x)


#5.find(),index(),rfind(),rindex()

# s="Python is easy"

# # x=s.index("z")
# # print(x)

# x=s.find("s",9,14)
# print(x)

# x=s.rfind("y")
# print(x)

# #x=s.find("y")
# #x=s.find("eas")
# x=s.find("java")
# print(x)


#4.Removing spaces rstrip(),lstrip(),strip()


# state1=input("Enter state:")
# #state=state1.lstrip()
# #state=state1.rstrip()
# state=state1.strip()

# if state=="Maharashtra":
#     print("Capital:Mumbai")
# elif state=="Gujarat":
#     print("Capital:Gandhinagar")
# elif state=="Uttar pradesh":
#     print("Capital:Lucknow")
# else:
#     print("Invalid state")
#
# 3.#comparision op
# s1="python"
# s2="Python is easy"
# print(s1<s2)

#2.Membership op in not in

# s1="Python is easy"
# print("Python" not in s1)

#1 .Mathematical op + *

# s1="Python"
# s2="Java"
# print(s1+s2)
# print(s1*3)
# print(len(s1))



"""

s="Python is easy"
#print(s[30])
#print(s[2:30:-1])
print(s[-2:-10:-1])
"""

"""

s="Python is easy"
print(s)
print("address=",id(s))
s="Java"
print(s)
print("address=",id(s))
"""

