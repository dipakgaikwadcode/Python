#list -- mutable

#cloning (using slicing and copy)

# l6 = [10,20,30]
# l2 = l6[:]  #// l6=l2.copy()
# print("l6:",l6)
# print("l2:",l2)

# print("l6 address:",id(l6))
# print("l6 address:",id(l2))


# l6[2] = 100
# print("l6:",l6)
# print("l2:",l2)


#alising(=)

l6 = [10,20,30]
l2 = l6 
print("l6:",l6)
print("l2:",l2)

print("l6 address:",id(l6))
print("l6 address:",id(l2))


l6[2] = 100
print("l6:",l6)
print("l2:",l2)




#g.reverse(), sort()

# li =[10,5,40,49,39]

# li.reverse()
# li.sort()
# li.sort(reverse=True)
# print(li)





#f. remove(), pop(),pop(index), clear()

# k1 = [10,20, 30, 40,50,10,10,29]

# k1.remove(10)
# k1.pop()
# k1.pop(2)
# k1.clear()

# del k1 

# print(k1)





# l1 = [10,20,30]
# l2 = [40,50]

# l1.extend(l2)
# print(l1)


# l1.append(l2)
# print(l1)




# #e.extend()
# l1= [10,20,39,43]
# l2 = [49,56]

# l1.extend(l2)

# print(l1)




# #d.insert()
# li = [10,20,230,43,2,4,2]
# li.insert(2,100)
# li.insert(-2,100)



# #c.append()
# li= [10,30,39,29,45,43]
# li.append(2,100)
# li.append(-3,100)


# #b.index()
# li = [10,20,10,30,20,10,50,10]
# print(li.index(20))
# print(li.index(60))
# #a.count()

# li = [10,20,30,20,10,50,10]
# print(li.count(300))








# l1 = [10, 20, 30, 40, 50]

# for i in l1:
#     print(i)

# #while

# l1 = [10, 20, 30, 40, 50]

# i = 0
# while i < len(l1):
#     print(l1[i])
#     i += 1


# # #a. empty list

# # li = []
# # print(li)
# # print(type(li))

# # #b. Initialze 

# # li = [10,20,'python', 10]
# # print(li)
# # print(type(li))


# # #C.Dynamic input 

# # li = eval(input("Enter list of data: "))
# # print(li)
# # print(type(li))


# #D.list()
# # t = (10,20,30)
# # print(t)
# # print(type(t))

# # li=list(t)
# # print(li)
# # print(type(li))



# # #e.split()

# # s = "Python is easy"
# # # li = s.split()
# # # print(li)