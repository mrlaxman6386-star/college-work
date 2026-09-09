# that repeatedly accepts numbers from the user and calculates their sum. Terminate the loop using
# break when the user enters 0.
sum=0
for i in range (1,100):
    n=int(input("Enter your number :"))
    if n ==0:
        break 
    else:
        sum = sum+n
        print(f"the sum is : {sum}")