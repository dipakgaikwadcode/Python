#dictionary--mutable

#dictionary comprehansion



# d = {  x:x*x for x in range(1,6)}
# print(d)
# print(type(d))






# #Q1.write a program to take dictionary from the keyboared and print the sum of values?

# s = eval(input("Enter the dictionary : "))

# s =sum(d.values())
# print("sum=",s)

# #2.write a progran to find number of occueernce of each letter presesnt in the given string

# word = input("Enter string:")
# d ={}
# for x in word:




#10.update()
# d1 =  {1:"python", 2:"java"}
# d2={3:"DA"}
# d1.update(d2)
# print(d1)
# #9.setdefault()

# a1 = {1:"python", 2:"java"}
# a1.setdefault(3,"sql")
# a1.setdefault(2,"C")
# print(a1)





#8.copy()
# d1 = {1:"python", 2:"java"}
# d2=d1   assling 

# d2=d1.copy()
# d1[3] = 'DA'
# print(d2)
# print(d1)





# #7.keys , values, items
# d1 = {1:"python", 2:"java",'a':"apple"}
# print(d.keys())

# for v in d1.keys():
#     print(v)




#6.pop(k) , popitem()

# d1 = {1:"python", 2:"java",'a':"apple"}

# x = d1.popitem()
# print(x)



# #pop()
# x = d1.pop(2)
# print(x)








#5.get(k),get(k,default)
# d={1:"Python",2:"Java",'a':"Apple"}
#x=d.get('a')
#x=d[5]
#x=d.get(5) #returns None
# x=d.get(5,"guest")
# print(x)


#4.del key,clear
# d={1:"Python",2:"Java",'a':"Apple"}
# print(len(d))
# d.clear()
# print(d)
# # del d[2]
# # #del d
# # print(d)

#3.update key
# d={1:"Python",2:"Java",'a':"Apple"}
# d[1]="Ds"
# print(d)
# d[3]="Net"
# print(d)


#2.accessing
# d={1:"Python",2:"Java",'a':"Apple"}
# for k in d:
#     print(k)


# d={1:"Python",2:"Java",'a':"Apple"}
# print(d[2])
# d[2]="DA"
# print(d)

#1.create dictionary
#e.
# d={}
# print(d)
# d[1]="Python"
# print(d)

#d.dynamic input
# d=eval(input("Enter data:"))
# print(d)
# print(type(d))

#c.dict()
# d=dict([(1,"Python"),(2,"Java"),(3,"DA")])
# print(d)
# print(type(d))

#b.initialise
# d={1:"Python",2:"Java",'a':"Apple"}
# print(d)

#a.empty dict
# d={}
# print(d)
# print(type(d))