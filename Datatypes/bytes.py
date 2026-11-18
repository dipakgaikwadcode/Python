#1.Bytes - immutable

#bytes doest show the real value in print

#range 0 to 256
'''
x = [10,20,30]
print(x)
print("Datype of x",type(x))


b = bytes(x)
print("b=",b)
print("Datatype of b",b)
print(b[1])
 # b[1] = 100 'bytes' object does not support item assignment
'''

#2.bytearray - mutable

 '''
x = [10,20,30]
print(x)
print("Datype of x",type(x))


ba = bytearray(x)
print("b=",b)
print("Datatype of b",b)
print(b[1])

ba[1] = 100
print(ba)

'''
# ba[1] = 100 'bytearray' object allow support item assignment



#3.list --- mutable

'''
li=[]
print("li=",li)

print("datatypes of li=",type(li))
'''


#tuple ---immutable
'''

t = ()  #round bracket

t2 =(10,20,"python", True)    #that both are tuples with bracket without bracktet
t1 = 10,20,"python", True


t4 = (10)
print(type(t))   # it is a integer beause there is only one value if you want to make it tuple we have to take  a , after that one value  like r =(10,)

'''
#5.range() ---immutable

r1 = range(0,52,2)
for i in r1:
    print(i)

    

















