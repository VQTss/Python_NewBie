import math
a=float(input())
b=float(input())
c=float(input())

if (a+b >c) == True and (a+c >b) == True and (c+b >a) == True:
    if a == b  and b == a and c == b:
        print("Equilateral triangle !")
    elif (a == b and a == c) or (c == b and c == a) or (b == a and b == c):
        print("Isosceles triangle !")
    elif (a**2 == b+c ) or (b**2 == a+c ) or (c**2 == a+b ):
        print("Right triangle !")
    elif math.degrees(tan(a/c)) > 90 or math.degrees(tan(c/b)) > 90 or math.degrees(tan(b/a)) > 90:
        print("Obtuse triangle !")
    else:
        print("Acute triangle !")
else:
    print("Not a Triangle !")
    