import math
def func1(x1,x2,x3):
    R=12*(pow(x1,2)+math.sin(x2))+ math.sqrt(pow(x3,2)+1)/math.log(math.fabs(math.fabs(x3)+7),3)
    return(R)
x1=float(input("Введіть x1:"))
x2=float(input("Введіть x2:"))
x3=float(input("Введіть x3:"))
R=func1(x1,x2,x3)
print(R)