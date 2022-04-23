
# Tuple Unpacking 
a,b,*c, d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(d)
fruits = ("apple", "banana", "cherry")
green, yellow, red = fruits
print(green)
print(yellow)
print(red)
# Tuple 
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
# Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
# Access Tuple Negative
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
# Range of index
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#Change Tuple Value
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#Append Item
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)



