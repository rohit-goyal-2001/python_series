thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
print(thisdict)
print(type(thisdict))
x = thisdict.get("model")
print(x)
x = thisdict.keys()
print(x)
x  = thisdict.values()
print(x)
#change item
thisdict["year"]  = 2017
print(thisdict)
thisdict.update({"year":"220220"})
print(thisdict)
#add items
thisdict["color"] = "b;ack"
print(thisdict)
#remove item
thisdict.pop("color")
print(thisdict)
for c in thisdict:
    print(c)

for c in thisdict.keys():
    print(c)    