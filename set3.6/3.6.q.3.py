# Write a function is_even(n) that returns True if the number is even, otherwise False.
def even(n):
    if n%2==0:
        return "Even"
    else:
        return "Not an even"
a=int(input("Enter a number: "))
print(even(a))