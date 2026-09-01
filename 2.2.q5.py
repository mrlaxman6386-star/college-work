#To sum the series ---- 1+1/2+1/3+1/4+........+1/n

n=int(input("Enter your number here : "))
i=1
sum=0
while (i<n+1):
    sum=sum+(1/i)
    i+=1
print(sum)
     