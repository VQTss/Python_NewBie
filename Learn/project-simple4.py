for row in range(6):
    for col in range(7):
        if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
            print(" * ", end="")
        else:
            print("  ",end="")
    print()
    # ------------------------------

str1 = input("Enter a string: ")
so_tu=1

for i in range(len(str1)):
    if(str1[i]==' '):
        so_tu=so_tu+1
print("Total words: ",so_tu)