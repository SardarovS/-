import math
x=float(input("Введіть значення Х:"))
if x>=3.7:
    y=x+x**(1/2)+(4*x+7)**1/3 
elif -1.5<x<3.7:
    y=math.tan(x)+x**2
elif x<=-1.5:
    y=math.log(math.fabs(x),math.e)
print(y)