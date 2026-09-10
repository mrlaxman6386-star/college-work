# Create a menu-driven program using functions:
# 1. Check Even/Odd
# 2. Check Prime
# 3. Find Factorial
# 4. Find Square
# 5. Exit
# Each operation must be implemented using a separate function.
def input_number():
    n=int(input("Enter a number here :"))
    return n
def even_odd(n):
    if n%2==0 :
        status="even number"
    else :
        status="odd number"
    return status
def prime(n):
    if n < 2:
        return "Not a prime number"

    for i in range(2, n):
        if n % i == 0:
            return "Not a prime number"

    return "Prime number"
def factorial(n):
    sum = 1
    for i in range (1,n+1):
        sum=sum*i
    return sum
def square(n):
    s= n*n
    return s
def menu():
    print("-----MENU-----")
    print("1.check even/odd")
    print("2.check prime or not")
    print("3.check factorial")
    print("4.square of a number")
    print("5.exit")

while True:

    menu()
    choice=int(input("Enter uor choice here :"))
    if choice==1:
      a=input_number()
      print(even_odd(a))
    elif choice==2:
        a=input_number()
        print(prime(a))

    elif choice==3:
      a=input_number()
      print(factorial(a))

    elif choice==4:
      a=input_number()
      print(square(a))

    elif choice==5:
      print("programme exited")
      break
    else:
      print("invalid choice")



