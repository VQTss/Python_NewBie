# from re import I


# def countdown():
#     i =5
#     while i > 0:
#         yield i 
#         i -= 1

# for i in countdown():
#     print(i)


# def infinite_sevens():
#     i  = 1
#     while i < 7:
#         yield i 
#         i += 1
        
# for i in infinite_sevens():
#     print(i)

# def function(name_arg,*arg):
#     print(name_arg)
#     print(arg)
    

# function(1,2,3,4,5)

def my_func(x,*arg,**kwargs):
    print(kwargs)

my_func(2,3,4,5,6,a=7,b=8)