#Instance Variable 

#declaring instance varible

#a.inside consttu

# class Test:
#     def __init__(self):
#         self.a=10

#     def m1(self):
#         self.b = 20  

#     def add(self) :
#         print("sum= ",self.a + self.b)


# t1 = Test()
# print("inst var: ",t1.__dict__)
# t1.m1()
# print("inst var: ",t1.__dict__)
# t1.add()


# # ___________________________________________________________

# t2 = Test()
# print("inst var: ",t1.__dict__)
# t2.m1()
# print("inst var: ",t1.__dict__)
# t2.add()


# print("t2 insta var: ",t2.__dict__)
# t2.y=100
# print("t2 insta var: ",t2.__dict__)

#accessing 
# class Test:
#     def __init__(self):
#         self.a = 10
#         print("a in constructor:",self.a)

#     def m1(self):
#         print("a is method:",self.a)


# t1= Test()
# t1.m1()
# print("a outside class:",t1.a)

#update 

# class Test:
#     def __init__(self):
#         self.a = 10
#         print("a in constructor:",self.a)

#     def m1(self):
#         self.a=100

# t1 =Test()
# t2 =Test()

# print("inst ver t1:",t1.__dict__)
# print("inst ver t2:",t2.__dict__)
# t1.m1()
# t2.m1()
# print("inst ver t1:",t1.__dict__)
# print("inst ver t2:",t2.__dict__)

# t2.a = 5555

# print("inst ver t1:",t1.__dict__)
# print("inst ver t2:",t2.__dict__)



# delete

# class Test:
#     def __init__(self):
#         self.a = 10
#         print("a in constructor:",self.a)

#     def m1(self):
#         print("a is method:",self.a)


# t1= Test()
# t2 = Test()


# print("inst ver t1:",t1.__dict__)
# print("inst ver t2:",t2.__dict__)

# print(
# )

# t1.m1()



#static variable ----

class Test:
    a = 10  #static variable
    def __init__(self):
        self.b=20   #instance variable 


print("a = ",Test.a)
t1=Test()
print("a using t1: ",t1.a)

