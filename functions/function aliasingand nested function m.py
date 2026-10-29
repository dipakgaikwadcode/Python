#nested function

def Outer():
    print("start of Outer")
    def Inner():
        print("I m in Inner function")
    print("End of Outer function")
    return Inner

inn=Outer()

inn=Outer



# inn=Outer()  #inn=Inner
# inn()

# def Outer():
#     print("start of Outer")
#     def Inner():
#         print("I m in Inner function")
#     Inner()
#     print("End of Outer function")
#
# Outer()



#function aliasing

# def f1(name):
#     print("Hello",name)
#
# f1("Tom")
# wish=f1  #function aliasing
# print("addressof f1:",id(f1))
# print("addressof wish:",id(wish))
# f1("Jack")
# wish("anna")