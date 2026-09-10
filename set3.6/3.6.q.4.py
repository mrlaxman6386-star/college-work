# Write a function maximum(a, b) that returns the larger of two numbers.
def maximum(a,b):
    if a > b:
        return a
    else:
        return b

a=int(input("Enter your first number here : "))
b=int(input("Enter your second number here : "))
print("your maximum number is :", maximum(a, b))