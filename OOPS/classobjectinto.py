
#6.constructor overloading
"""
constructor overloading not supported in python
The last constructor will be activated and all above constructor will be deactivated

# """
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __init__(self):
#        self.name="Vaishali"
#        self.age=38

#     def show(self):
#         print(self.name)
#         print(self.age)

# s1=Student()
# s1.show()



#5.---Constructor with arguement
# class Student():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#
#     def show(self):
#         print("self.name",self.name)
#         print("self.age",self.age)
#
#
# s1=Student(1,"Jack")
# #s1.show()

#4.---Constructor without arguement
# class Student:
#     def __init__(self):
#        print("this is a constructor")
#        self.rno=int(input("enter rno:"))
#        self.name=input("enter name:")
#        print()

#     def show(self):
#         print("rollno:", self.rno)
#         print("name:",self.name)


# s1=Student()
# s2=Student()
# print("************************")
# s1.show()
# print()
# s2.show()

# s1.__init__()
# s1.show()


# #3.
# class Student:
#     def accept(self,rno,name):
#         self.rno=rno
#         self.name=name

#     def show(self):
#         print("rollno:",self.rno)
#         print("name:",self.name)

# s1=Student()
   
# s1.accept(101,"dipak")    #you need to call accept before calling show otherwise will give attribute error
# s1.show()
# s1=Student()
# print("s1=",s1)
# rno=input("enter rno:")
# name=input("enter name:")
# s1.accept(rno,name)
# s1.show()
# print("__________________________")
# s2=Student()
# print("s2=",s2)
# s2.accept(102,"Jack")
# s2.show()


#1.
# class Test():
#     """ This is my first class"""
#     a=10
#     print(a)