try:
    # file = open("newfile.txt", "a")
    # Read file
    # for i in range(5):
    #     print(file.readline())
    # file.close()
    # file.write("This is been written to a file")
    # file.write("\n The Vinci Code")
   with open("newfile.txt", "r") as f:
       print(f.read())
except:
    print("Error")
finally:
    try:
        # file.close()
        f.close()
        print("Done")
    except:
        print("Error")