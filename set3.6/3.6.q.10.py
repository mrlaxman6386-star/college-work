# 10.Write a function factorial(n) that returns the factorial of a number.
def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
a=int(input("Enter a number: "))
print("The factorial of the number is :",factorial(a))