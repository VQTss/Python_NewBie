# cubes  = [i**3 for i in range(5)]
# print(cubes)
# evens  = [i**2 for i in range(10) if i**2 % 2 == 0]
# print(evens)

text = input()
dict = {}
#your code goes here

def hasKey(dict, char):
    for x in dict.keys():
        if x == char:
            return True
    return False    
    

for char in text:
    count  =  0
    if hasKey(dict,char) == True:
        item = dict[char]
        item += 1
        dict[char]  = item
    else:
         count += 1
         dict[char] = count
print(dict)

