file = open("demo.txt", "r")

#your code goes here
for str in file.readlines():
    arr = str.split(" ")
    for i in arr:
        print(f'{i[0]}',end='')
file.close()