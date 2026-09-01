#To print the multiplication table of n. where n is to be entered by the user.

n=int(input("Enter your number : "))
for i in range (1,11):
    print(f"{i}*{n}={i*n}")

#by while loop :
n=int(input("Enter your number : "))
i=1
while(i<11):
    s=n*i
    i +=1
    print(s)