class Test:
    def m1(self):
        def calc(n1,n2):
            print(f"{n1} - {n2}")
            print("Addition:",n1+n2)
            print("substraction:",n1-n2)
            print("multiplication:",n1*n2)
            print("*******************************")

        #calc(10,20)
        #calc(2,3)
        return calc


t1=Test()
f1=t1.m1()  #f1=calc   #function aliasing
f1(10,20)
