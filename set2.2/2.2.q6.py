#To generate the calendar of a month given the start day and no of days in the month.
s=int(input("Enter the start day of a month : "))
n=int(input("Enter the numbers of days in the month : "))
i=1

print(" "*s,end=" ")
while i<=n:
    print(i,end="  ")
    if (i+s)%7 ==0:
            print()
    i +=1