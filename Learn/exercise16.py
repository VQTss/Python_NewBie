
num = [1,2,3]
print(num + [4,5,6])
print(num*3)
# List operations  
words = ["spam","egg","spam","sausage"]
print("spam" in words)
print("egg" in words)
print("tomatos" in words)
print("tomatos" not in words)
numbers = list(range(10)) # end 10 - 1
print(numbers)
numbers = list(range(3,10)) # start from 3
print(numbers)
numbers = list(range(0,10,2)) # steps is 2
print(numbers)
squares = list(range(20))
print(squares[2:6])
print(squares[0:1])
print(squares[:7])
print(squares[7:])
squares = list(range(20))
print(squares)
print(squares[2:9:3])
print(squares[1::4])
print(squares[::-1])
print(squares[1:-1])
list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])
