# 20. Number Analysis Program: Create a program using separate functions:
# input_number(), check_even_odd(), check_prime(), find_factorial(),
# display_result()
# The program should accept a number and display all the required results.
def input_number():
    n=int(input("Enter a number here :"))
    return n
def check_even_odd(n):
    if n%2==0:
        return "Number is even"
    else:
        return "Number is odd"

def check_prime(n):
    for i in range (2,n):
        if n%i==0 and n<=1:
            return "Number is not prime"
        else:
            return "Not a prime number"
def find_factorial(n):
    sum = 1
    for i in range (1,n+1):
        sum=sum*i
    return sum
def display_result(n):
    a=check_even_odd(n)
    b=check_prime(n)
    c=find_factorial(n)
    print("==============================")
    print(a)
    print(b)
    print("factorial number is :",c)
    print("==============================")
a=input_number()
display_result(a)