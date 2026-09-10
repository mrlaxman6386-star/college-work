# 11.Write a function check_prime(n) that returns whether a number is prime or not.
def prime(n):
    if n < 2:
        return "not a prime number"
    
    for i in range(2, n):
        if n % i == 0:
            return "not a prime number"
    return "a prime number" 
a=int(input("Enter a number: "))
print(prime(a))