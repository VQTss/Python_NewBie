print("Phương trình phân loại học sinh")
a = float(input("Nhập điểm của học sinh: "))
if a >= 9.0:
    print("Học sinh giỏi")
elif a > 7.0 and a < 9.0:
    print("Học sinh khá")
elif a >= 5.0 and a < 7.0:
    print("Học sinh trung bình")
else:
    print("Học sinh yếu")