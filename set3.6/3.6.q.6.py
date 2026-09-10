# Write a function calculate(a, b) that returns the sum, difference, product, and
# division of two numbers.
def calculate(a, b):
    sum = a+b
    difference = a-b
    product = a*b
    division = a/b
    return sum , difference , product , division
    
a=int(input("Enter your first number here : "))
b=int(input("Enter your second number here : "))
print("Sum:", calculate(a, b)[0]) # if we dont apply index here then it will return a tuple of all the values 
print("Difference:", calculate(a, b)[1])
print("Product:", calculate(a, b)[2])
print("Division:", calculate(a, b)[3])