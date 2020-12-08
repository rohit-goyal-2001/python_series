#Tuple items are ordered, unchangeable, and allow duplicate values.
t1 = ("a","b","c","d","e","f")
print(t1)
t2 = ("t3","t3","t3")
print(t2)
print(len(t2))
t5 = ("roht")#not a tuple
t6 = ("rohit",)# tuple hai
tuple1 = ("abc",23,"r",False)
print(type(tuple1))
'''List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered and changeable. No duplicate members.'''
print(tuple1[1])
print(tuple1[1:3])#include 1 not 3
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1)
print(tuple1[0:])
print(tuple1[-3:-1])#not include -1 and include 3
#change tuple values
y = list(tuple1)
y[1] = "rojhitt"
y.remove("r")
x= tuple(y)
print(x)
print(tuple1)
(green,yello,black,white)  = tuple1
print(green)
(green,*yello,red)  = tuple1
print(*yello)

for c in tuple1:
    print(c)

for x in range(len(tuple1)):
    print(tuple1[x])


tuple2 = t1+t2
print(tuple2)    