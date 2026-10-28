
#list --mutable

#3.built-in functions

#h.aliasing and cloning
#cloning  (using slicing and copy)
l1=[10,20,30]
#l2=l1[:]
l2=l1.copy()
print(l1)
print(l2)
print("l1 address:",id(l1))
print("l2 address:",id(l2))
l1[2]=100
print(l1)
print(l2)

#aliasing  (=)
# l1=[10,20,30]
# l2=l1
# print(l1)
# print(l2)
# print("l1 address:",id(l1))
# print("l2 address:",id(l2))
# l1[2]=100
# print(l1)
# print(l2)
#




#g.reverse(),sort()

# l1=[10,5,40,30,25]
# #l1.reverse()
# #l1.sort()
# l1.sort(reverse=True)
# print(l1)


#f.remove(),pop(),pop(index),clear()
# l1 = [10, 20, 10, 30, 20, 10, 50, 10]
# #l1.remove(10)
# #l1.remove(55)
# #l1.pop()
# #l1.pop(2)
# #l1.clear()
# #del l1[4]
# del l1
# print(l1)


#create a list of even numbers from 1 to 100
# which are divisible by 7
# l1=[]
# for x in range(101):
#     if x%2==0 and x%7==0:
#         l1.append(x)
# print(l1)
#
# # for x in range(0,100,2):
# #     if x%7==0:
# #         l1.append(x)
#
# print(l1)



#e.extend()
#l1 = [10, 20, 10, 30, 20]
#l2= [50,60]
#l2=4,5,6
# l2="Java"
# l1.extend(l2)
# print(l1)
#

#d.insert()
# l1 = [10, 20, 10, 30, 20, 10, 50, 10]
# #l1.insert(2,100)
# l1.insert(-3,100)
# print(l1)

#c.append()
# l1 = [10, 20, 10, 30, 20, 10, 50, 10]
# l1.append("Python")
# print(l1)

#b.index()
# l1=[10,20,10,30,20,10,50,10]
# print(l1.index(20))
# #print(l1.index(60))


#a.count()

# l1=[10,20,10,30,20,10,50,10]
# print(l1.count(300))



#2.Accessing elements

l1=[10,20,30,40,50]
#Traversing(for or while)

# l=len(l1)
# i=0
# while(i<l):
#     print(l1[i])
#     i+=1


# for i in l1:
#     print(i)


#slicing
# print(l1[::-1])
# print(l1[-2:-8:-1])

#index
# print(l1[3])
# #print(l1[20])
# print(l1[-2])



#1.create list
#e.split()
# s="Python is easy"
# l1=s.split()
# print(l1)

#d.list()
# t=(10,20,30)
# print(t)
# print(type(t))
# l1=list(t)
# print(l1)
# print(type(l1))



#c.Dynamic input

# l1=eval(input("enter list of data:"))
# print(l1)
# print(type(l1))

#b.Initialize

# l1=[10,20,"Python",10]
# print(l1)
# print(type(l1))


#a.empty list

# l1=[]
# print(l1)
# print(type(l1))








# l1=[10,20,30]
# l2=[10,20,30]
# print(l1 is l2)  #False
# print(l1==l2) #True