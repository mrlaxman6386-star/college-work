#To calculate the power(x,n).
a1=int(input("Enter the value of x : "))
a2=int(input("Enter the value of n : "))
i=1
power=1
while (i<=a2):
    power=power*a1
    i +=1
print("x raised to the power n is : ",power)