# def cal_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False

# n =  int(input())
# print(cal_year(n))
"""Fibonacci use loop"""
def fibonacci(n):
	f0=1
	print(f0)
	f1=1
	print(f1)
	for i in range(2,n+1):
		f=f0+f1
		print(f)
		f0=f1
		f1=f

number = int(input("Nhập số nguyên: "))
fibonacci(number)
"""Ti le vang fibonacci"""
def golden_rate(n):
	f0=1
	f1=1
	for i in range(2,n):
		f=f0+f1
		print(f/f1)
		f0=f1
		f1=f

number = int(input("Nhập số nguyên: "))
golden_rate(number)