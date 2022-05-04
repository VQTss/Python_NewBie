# dict used to  store data values in key:value pairs
# ordered are items have defined order, that order will not change
# changeable and do not allow duplicates
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
a = {'key': [1,2,23,4]}
print(a)
# len in dict
print("This is length of dicts: ", end='')
print(len(thisdict))
print("Items has key is brand will value is: ",end='')
print(thisdict["brand"])
# get used to take value of key
x = thisdict.get("model")
print("keys() method will return a list all keys in the dictionary", end='')
print( thisdict.keys())
print("values() method will return a list all values in the dictionary", end='')
print( thisdict.values())
# Update key:values
thisdict['color']  ='red'
print("After update key:value into dict:",thisdict.keys())
#Change item
thisdict["year"] = 2018 # or
# thisdict.update({"year": 2020})
print(thisdict)
# remove the item
thisdict.pop("model") # or
# del thisdict["model"] # remove the item with  the specified key name
# remove the last item
thisdict.popitem()

