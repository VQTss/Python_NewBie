# Tuples is a collection which is order and unchangeabl
# Unchangeable cannot change add or remove 
# init tuples way 1
this_tuple1 = ("aplle",12,"banana",15)
print(this_tuple1)
# init tuples way 2
this_tuple2 = tuple(("mango",10,"cherry",20))
print(this_tuple2)
# Access tuple item
thistuple3 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple3[:4]) # start 0 and end 4
print(thistuple3[-1]) #  last item  
print(thistuple3[-4:-1]) # đi từ phía sau lên phía trước nghĩa là đi từ phải qua trái trong tuple

#Unpack tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Join tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
print(tuple1*2)