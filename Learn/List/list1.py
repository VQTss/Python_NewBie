# Way 1
list_text1 = ["Cristino Ronado",'37',"MU-FC"]
# Way 2
list_text2 = list(("Leo Messi",35,"PSG-FC"))
print("There are two list")
print(list_text1)
print(list_text2)
# append  used to add item into list
list_text1.append(100)
list_text2.append(['Juventus','30'])
print("List after used to function append()")
print(list_text1)
print(list_text2)
# extend use to add multiple item into list
list_text1.extend(['Baca-FC',18])
list_text2.extend(['Sporting-FC'])
print("List after used to function extend()")
print(list_text1)
print(list_text2)
# pop used to remove item at the specified position
print("List afer used to function pop")
list_text1.pop(len(list_text1) - 1) # remove last item
list_text2.pop(0) # remove first item
print(list_text1)
print(list_text2)
# copy used to copy a list into another list
newlist = list_text1.copy()
print("New list: ",end='')
print(newlist)






