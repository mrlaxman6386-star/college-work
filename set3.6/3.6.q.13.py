# 13.Write a function sum_of_digits(n) that returns the sum of digits of a number.
def sum_of_function(n):
    total = 0

    while n>0:
       digit= n%10
       total = total + digit 
       n = n//10
    return total

a=int(input("enter your number here : "))
print(sum_of_function(a))