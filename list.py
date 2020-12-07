mylist  = ["rohit","mohit","goyal","diwedi"]
#List items are ordered, changeable, and allow duplicate values.
print(mylist)
print(len(mylist))
list1  = [1,2,3,4,5,6,7,8,9]
print(len(list1))
print(type(list1))
#create list using constructor
thislist =  list(("r","m","o"))
print(len(thislist))
#acess list item
#mutable object can be changed after it is created
#list are mutable
list4 = ["rohit","rohit","mohiiii","jiigig","jii","rohit","rohit","hiiii","huutut"]
print(type(list4))
print(list4[1])
print(list4[-1])
print(len(list4))
print(list4[2:5])
print(list4[::-1])
print(list4[-5:-1])
#change list item,yeha list zero se count hoti h 
list4[1] = "blackcurrent"
print(list4)
list4[1:3]  = ["like","by"]
print(list4)
list4.insert(1,"kanu")
print(list4)
#add item in list
list4.append("orange")
print(list4)
list4.extend(thislist)
print(thislist)
print(list4)
#remove item
list4.remove("orange")
print(list4)
del list4[0]
print(list4)
list4.pop(1)
print(list4)
list4.pop()#take from last
print(list4)
#   del list4  #delete complete  list
#list4.clear() clear list data
print(list4)

#loop in list
for i in range(len(list4)):
    print(list4[i])

i= 0;
while i< len(list4):
    print(list4[i])
    i = i+1;

#sorting of list
list4.sort()    
print(list4)
list4.reverse()
print(list4)   
#copy of list
list7  = list(list4)
print(list7) 