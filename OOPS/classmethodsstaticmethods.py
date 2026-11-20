#Points to remember
class Test:
    def __init__(self):
        self.y=100

    def mthd(cls):
       print(cls)

Test.mthd("Hello")

# t1=Test()
# t1.mthd()








#2.staticmethod
# class Test:
#     x=200
#     def __init__(self):
#         self.y=100
#
#     @staticmethod
#     def stsmthd(a,b):
#        print("Addition:",a+b)
#
# t1=Test()
# t1.stsmthd(10,20)
# Test.stsmthd(50,60)
#
#



#**********************************************************************************
#.DISPLAY NO OF OBJECTS

# class Test:
#     count=0
#     def __init__(self):
#         Test.count+=1
#
#     @classmethod
#     def countobj(cls):
#         print("no of objects:", Test.count)
#
# t1=Test()
# t2=Test()
# Test.countobj()
# t3=Test()
# t4=Test()
# Test.countobj()
#


#1.classmethods

#.
# class Test:
#     def __init__(self):
#         self.a=10
#
#     def m1(self):
#         print("self:",self)
#         print("a=",self.a)
#         print("-------------------------------")
#
#     @classmethod
#     def clsmthd(cls):
#         print("cls:",cls)
#         Test.x=100
#         cls.y=200
#
# Test.clsmthd()
# t1=Test()
# t1.m1()
# t1.clsmthd()
