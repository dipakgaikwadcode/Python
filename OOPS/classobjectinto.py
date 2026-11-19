
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






# class Student:
#     collage_name = "ABC collage"
    

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("additing new student in database..")


# s1 = Student("karan",76)
# print(s1.name)
# print(s1.collage_name)


# print("=================")

# s2 = Student("",76)
# print(s2.name)
# print(s2.collage_name)




# Q4. Rectangle

# Create a Rectangle class.
# - Create a method area(self, length, width).
# - Calculate the area.
# - Print the result.


# class Rectangle :
#     def __init__(self,length,width):
#          self.lenght = length
#          self.width = width
#          result = self.lenght * self.width  
#          print(f"the area of the rectangle is : {result}")
        
        
# s = Rectangle(23,43)

# Q5. Bank Account

# Create a Bank class.
# - Create a method deposit(self, amount).
# - Create a method withdraw(self, amount).
# - Create a method balance(self).
# - Maintain the balance using self.

# class Bank:

#     def __init__(self,amount):
#       self.amount = amount
    
    
#     def deposit(self,amount):
#      self.amount+=amount

#     def withdraw(self, amount):
#       self.amount-=amount
      
#     def balance(self):
#         print("current amount:",self.amount)


# z1 = Bank(24500)

# z1.deposit(1000)
# z1.withdraw(5500)
# z1.balance()


# Q6. Marks Calculator
# Create a Student class.
# - Create a method accept(self, name, m1, m2, m3).
# - Create a method total() to calculate total marks.
# - Create a method percentage() to calculate percentage.


class Student:
    def acceptgive(self,name,m1,m2,m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total(self):
        self.totalmarks = self.m1+self.m2+self.m3
        print("Student name:",self.name)
        print("totalmarks:",self.totalmarks)

    def percentage(self):
        percen = (self.totalmarks / 3) * 100
        print("total percenatage :",percen)



h1 = Student()

h1.acceptgive("dipak",97,87,76)
h1.total()
h1.percentage()