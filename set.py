myse  = {"rohit","mohit","goyal"}
print(myse)
print(len(myse))
#print(myse[1]) not working in set
for c in myse:
    print(c)
print("rohit" in myse)    
myse.add("kanu")
print(myse)
t1 = {1,2,3}
myse.update(t1)
print(myse)

myse.remove("rohit")
print(myse)
print(myse.pop())
print(myse)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)#add all but not duplicate

print(x)