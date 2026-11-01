# # position arguement 

# def person(name,age):
#     print(f"hello buddy im {name} and im {age} years old.!")

# person("dipak",22)

# #keyword arguments


# def person(name,age):
#     print(f"hello buddy im {name} and im {age} years old.!")

# person(age = 22 , name = "dipak")



#varible length arguemnt

def summ(*n):
    print(n)

summ()
summ(10)
summ(10,20)
summ(10,20,30)