


x = lambda a : a + 10
print(x(5))
#name function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(1))
#lambda
sum  = lambda x : x**2 + 5*x + 4
print(sum(1))
#lambda
print((lambda x : x**2 + 5*x + 4)(1))
# map function
def add_five(x):
    return  x + 5
nums = [11,22,33,44,55]
result = list(map(add_five,nums))
print(result)

# filter
nums = [11,22,33,44,55]
res  = list(filter(lambda x : x % 2 == 0,nums))
print(res)
