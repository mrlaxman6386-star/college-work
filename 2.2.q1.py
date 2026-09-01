#To calculate average of first n natural numbers. Where n is to be entered by the user.

n=int(input("Enter the value : "))
i=1
sum=0
for i in range (0,n+1):
    sum=sum+i
    i +=1
print(sum)

