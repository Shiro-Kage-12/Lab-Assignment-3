#program to convert a number to its binary equivalent
print("Enter a number")
num = (int)(input())
num1 = num
num_exp = 0
rem = 0
num_bi = 0
while(num1>0):
    rem= num1%2
    num_bi = (int)(num_bi + (rem*10**num_exp))
    num1 = num1//2
    num_exp+=1
print("The binary equivalent of ",num,"=",num_bi)