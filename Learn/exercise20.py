# n  = int(input())
# for i in range(n):
#     print(i**2)
def vi_du():
    a = 100

    def vi_du2():
        global a
        a = 1
    
    print("Giá trị của biến a là:", a)
    vi_du2()
    print("Giá trị của biến a sau khi gọi hàm được lồng bên trong là:", a)

vi_du()
print("Giá trị của biến a bên ngoài hàm là:",a)