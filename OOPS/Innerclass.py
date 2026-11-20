# class Outer:
#     def __init__(self):
#         print("Outer classs constructor")

#     class Inner:
#         def __init__(self):
#             print("Inner classs constructor")

#         def m1(self):
#             print("Inner class instmethod m1")

#     def m2(self):
#         print("Outer class instmethod m2")

# #Outer().m2()
# Outer().Inner().m1()

# # o1=Outer()
# # o1.m2()
# # inn=o1.Inner()
# # inn.m1()


# # inn=Inner()
# # inn.m1()



class Person():
    def __init__(self,name,dd,mm,yyyy):
        self.name = name
        self.dob = self.Dob(dd,mm,yyyy)

    def display(self):
        print("Hai: ",self.name)
        self.dob.dob()

    def Dob():
        def __init__(self,dd,mm,yyyy):
            self.dd=dd
            self.mm = mm
            self.yyyy = yyyy

    # def dob(self):
    #     print("your birth day is on {}/{}/{}",.format)