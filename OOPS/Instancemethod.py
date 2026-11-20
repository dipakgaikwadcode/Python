class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        print("sum=",self.a+self.b)
        self.sub()

    def sub(self):
        print("sub=",self.a-self.b)

c1=Calculator(30,20)
c1.add()
print()
