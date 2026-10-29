#5.Keyword-variable length arguement

def show(**kwargs):
    print(kwargs)

show(name="tom",age=20)
show(name="tom",age=20,sal=20000)

#4.Variable length arguement

# def summ(*n,name):
#     total=0
#     for x in n:
#         total+=x
#     print("name:",name)
#     print("total:",total)
#
# summ(10,20,30,name="Tom")


# def summ(*n):
#     total=0
#     for x in n:
#         total+=x
#     print("total:",total)
#
# summ()
# summ(10)
# summ(10,20)
# summ(10,20,30)


#3.default arguement
# def person(name="guest",age=0):
#     print(f"{name} is of age {age} years old.")
#
# person("Tom",20)
# person()




#2.keyword arguements

# def person(name,age,sal):
#     print(f"{name} is of age {age} years old and earning sal of {sal}.")
#
# person("Tom",sal=20000,age=23)



#1.Positional arguemnet

# def person(name,age):
#     print(f"{name} is of age {age} years old.")
#
# person("Tom",20)
