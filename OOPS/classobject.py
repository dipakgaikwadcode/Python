
# class Students:
#     def accept(self,rno,name):
#         self.rno=rno
#         self.name=name

#     def show(self):
#         print("rollno:",self.rno)
#         print("name:",self.name)


# s1=Students()
# print("s1=",s1)

# s1.accept(101,"dipak")

# s1.show()


# class Employees:
#     def accept(self):
#         self.emp_id = emp_id
#         self.emp_name = emp_name
#         self.emp_salary= emp_salary

#     def show(self):
#         print("employee name :",self.emp_name)
#         print("employee id",self.emp_id)
#         print("employee salary",self.emp_salary)


# emp_id = input("Enter id: ")
# emp_name = input("Enter name: ")
# emp_salary = input("Enter salary: ")



# e1= Employees()
# e1.accept()
# e1.show()

# # ------------------------------------


# e2= Employees()
# e2.accept()
# e2.show()


# # -----------------


# e3= Employees()
# e3.accept()
# e3.show()



# without parameter


# class Student:
#     def __init__(self):
#         print("this is a constractor")
#         self.rno=int(input("Enter rno: "))
#         self.name =input("Enter name : ")
#         print()

#     def show(self):
#        print("rollno:",self.rno)
#        print("name:",self.name)


# s1=Student()
# s2=Student()
# print("*******************")


# s1.show()
# print()
# s2.show()



# class Student():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def show(self):
#         print("self.name: ",self.name)
#         print("self.age: ",self.age)

# s1=Student("dipak",129)
# s1.show()




#create a class calculataor 
# create 2 instance veriable 
# craete 4 intance method
# add
# sub
# Multi
# division


# class Calculator():
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def add(self):
#        add = self.a + self.b
#        print("addition: ",add)

#     def sub(self):
#         sub = self.a - self.b
#         print("subtraction: ",sub)

#     def mul(self):
#             mul = self.a * self.b
#             print("multiplation: ",mul)
#     def div(self):
#             div = self.a / self.b
#             print("division: ",div)

        
# a = int(input("Enter the value of A :"))
# b = int(input("Enter the value of B :"))




# choice = int(input("Enter the choice number :"))



# d1 = Calculator(a,b)
# d1.add()
# print()
# d1.sub()
# print()
# d1.mul()
# print()
# d1.div()
# print()


 
# Level 1 – Easy
# Q1. Without extra arguments

class Studentname:
    def name(self):
        name = "dipak"
        print(name)
     
# a = Studentname()
# a.name()

# Create a Student class with a show() method that prints:
# - Name: Dipak
# - Age: 22
# - City: Pune
# Q2. With arguments

# class Student():
#  def collage(self):
#     self.name = "Dipak"
#     self.age = 22
#     self.city = "pune"

#  def show(self):
#     print("The name of Student is : ",self.name)
#     print("The age : ",self.age)
#     print("The city : ",self.city)


# a = Student()
# a.collage()
# a.show()
# Create an Employee class with an accept() method that accepts employee ID and name. Create an object and display the details.

# Q3. With arguments

# Create a Calculator class with an add() method that accepts two numbers and prints their addition.
# Level 2 – Medium
# Q4. Default arguments

# Create a Student class with a show() method.
# - Default name = Dipak
# - Default age = 22
# - Try calling it without arguments.
# - Try calling it with different arguments.
# Q5. Variable-length arguments (*args)

# Create a Calculator class with a method that accepts multiple numbers and prints their sum.

# Example: 10, 20, 30, 40, 50

# Q6. With arguments

# Create a Bank class with:
# - deposit(amount)
# - withdraw(amount)
# - show_balance()
# Maintain the balance using an instance variable.
# Level 3 – Challenge
# Q7. Without extra arguments

# Create a Car class with a start() method that prints the car's starting message.

# Q8. Default arguments

# Create a Product class with a method accepting:
# - Product name
# - Price (default ₹500)
# Q9. Variable-length arguments

# Create a Student class that accepts multiple subject marks using *args and calculates the average.



# class Budy:
#    def accept(self):
#       print("self: ",self)
#       pass
#    def show(self):
#       pass

# s = Budy()
# print("s1=",s)
# s.accept()


# print("---------------------------")

# s2 = Budy()
# print("s2= ",s2)
# s2.accept()













class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("additing new student in database")


s1=Student("dipak",97)
print(s1.name,s1.marks)