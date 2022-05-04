# A set is a collection which is unordered , unchangeable but can remove and add items
set_demo1 = set((10,8,9,7,10,9))
print(set_demo1)
set_demo2 = {1,2,3,4,1,2,3}
print(set_demo2)
# Add item 
set_demo1.add(11)
print(set_demo1)
set_demo2.add(12)
print(set_demo2)
# Update
list_demo = [1,2,3,4,1,2,3]
set_demo1.update(list_demo)
print(set_demo1)
# remove
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
thisset1 = {"apple", "banana", "cherry"}
thisset1.remove("banana")
print(thisset1)
# Find
print( 1 in set_demo2)
print(set_demo1.union(set_demo2))
print(set_demo1.difference(set_demo2))
print(set_demo1.intersection(set_demo2))


