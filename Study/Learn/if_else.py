# n  = float(input("Nhap vao trung binh cua cac mon hoc: "))
# # diem trung cua dai hoc quoc gia ha noi
# #khoa tin hoc > 7.5 -> pass 
# if n >= 7.5:
#     print("Ban da pass dai hoc quoc gia")
# else:
#     print("Ban da truot")

print("So sanh 2 a va b")
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
if a < b:
    print(f"Result: a < b = {a} < {b}")
elif a == b:
    print(f"Result: a = b = {a} = {b}")
else:
    print(f"Result: a > b = {a} > {b}")
