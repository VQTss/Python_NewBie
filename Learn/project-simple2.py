#  Công thức A = P * (1 + r/n)^nt
p = float(input("Số tiền gốc ban đầu: "))
t = float(input("Số năm cho vay: "))
r = float(input("Lãi suất hằng năm: "))
n = float(input("Số lần ghép lãi trong một năm: "))
a = p * (1+(r/n))**(n*t)
print("Tổng số tiền là: ",a)