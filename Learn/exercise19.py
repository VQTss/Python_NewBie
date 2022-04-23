str1 = input()
str2 = input()
count = 0
for i in range(len(str1)):
    t = i +  len(str2)
    if t <= len(str1):
        a = str1[i:t]
        if a == str2:
            count += 1

print(count)
    

        

