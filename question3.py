# program to evaluate given mathematical expressions
# 1. (3+4)(5)
import math
result1 = (int) ((3+4)*(5))
print(" (3+4)(5) = ",result1)
# 2. n(n-1)/2
print ("Enter the value of n")
n= (int)(input())
result2 = n * (n-1)/2
print ("n(n-1)/2 = ",result2)
# 3. 4πr^2
print ("Enter the value of r")
r = (int)(input())
result3 = 4 * math.pi * r**2
print (" 4"+'\u03C0'+"r^2=",result3)
# 4. [r(cos a)^2 + r(sin b)^2]^0.5
print ("Enter the value of r")
r= int(input())
print ("Enter a and b")
a= int(input())
b= int(input())
result4 = math.sqrt(r * (math.cos(a))**2 + r * (math.sin(a))**2)
print ('\u221A'+"r(cos a)^2 + r(sin b)^2 =", result4)
# 5. (y2-y1)/(x2-x1)
print("Enter y1")
y1= int(input())
print("Enter y2")
y2= int(input())
print("Enter x1")
x1= int(input())
print("Enter x2")
x2= int(input())
result5 = (y2-y1)/(x2-x1)
print(" (y2-y1)/(x2-x1) = ",result5)