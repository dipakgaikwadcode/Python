#Instance Variable
#4.delete instance variable

# class Test:
#     def __init__(self):
#         self.a=10

#     def m1(self):
#        del self.a

# t1=Test()
# t2=Test()
# print("inst var t1:",t1.__dict__)
# print("inst var t2:",t2.__dict__)
# #t1.m1()
# del t2.a
# print("inst var t1:",t1.__dict__)
# print("inst var t2:",t2.__dict__)

#3.update Instance variable
# class Test:
#     def __init__(self):
#         self.a=10
#
#     def m1(self):
#        self.a=100
#
# t1=Test()
# t2=Test()
# print("inst var t1:",t1.__dict__)
# print("inst var t2:",t2.__dict__)
# t1.m1()
# t2.m1()
# print("inst var t1:",t1.__dict__)
# print("inst var t2:",t2.__dict__)
# t2.a=5555
# print("inst var t1:",t1.__dict__)
# print("inst var t2:",t2.__dict__)

#2.Accessing Instance variable

# class Test:
#     def __init__(self):
#         self.a=10
#         print("a in constructor:",self.a)
#
#     def m1(self):
#         print("a in method:", self.a)
#
#
# t1=Test()
# t1.m1()
# print("a outside class:",t1.a)




#1.Declaring instance variable

#b.Outside the class using reference variable
# class Test:
#     def __init__(self):
#         self.a=10

#     def m1(self):
#         self.b=20

#     def add(self):
#         print("sum=",self.a+self.b)
# t1=Test()
# t1.m1()
# print(" t1 inst var:",t1.__dict__)
# t1.add()
# print("________________________")
# t2=Test()
# t2.m1()
# print(" t2 inst var:",t2.__dict__)
# t1.c=100 #declaring with t1
# print(" t1 inst var:",t1.__dict__)
# print(" t2 inst var:",t2.__dict__)
# t2.y=500 #declaring with t2
# print(" t1 inst var:",t1.__dict__)
# print(" t2 inst var:",t2.__dict__)


#a.inside constructor and inside instance method

# class Test:
#     def __init__(self):
#         self.a=10

#     def m1(self):
#         self.b=20

#     def add(self):
#         print("sum=",self.a+self.b)



# t1=Test()
# print("inst var:",t1.__dict__)
# t1.m1()
# print("inst var:",t1.__dict__)
# t1.add()

# print("________________________")
# t2=Test()
# print("inst var:",t2.__dict__)
# t2.m1()
# print("inst var:",t2.__dict__)



# examples



