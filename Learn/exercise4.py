a = 3586
b = 952
print("Tổng của " + str(a) +  " + " + str(b) + " là: " +str(int(a+b)))
print("Hiệu của " + str(a) +  " - " + str(b) + " là: " +str(int(a-b)))
print("Tích của " + str(a) +  " * " + str(b) + " là: " +str(int(a*b)))
print("Thương của " + str(a) +  " / " + str(b) + " là: " +str(int(a/b)))
print(str(a) + " chia " + str(b) +" dư là: "+ str(int(a%b)))

print("--------------------------------------------------")
a  = 200 * (1.08**10)
print("Số tiền của bạn sau 10 năm là: "+ str(a))
print("--------------------------------------------------")
# Hàm eval 
print(eval('100 + 200'))