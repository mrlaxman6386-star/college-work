# Simple Calculator: Organise a calculator program using separate functions: add(),
# subtract(), multiply(), divide()
# The main program should ask the user for two numbers and an operation.

def main():
    number= []
    for i  in range(1,3):
        a=int(input("Enter your number here :"))
        number.append(a)
    return number
def add(a):
    return a[0]+a[1]
def subtract(a):
    return a[0]-a[1]
def multiply(a):
    return a[0]*a[1]
def divide(a):
    return a[0]/a[1]
a=main()
c=input("Enter your choice here :").lower()
if c == "add":
    print(add(a))
elif c == "subtract":
    print(subtract(a))
elif c== "multiply":
    print(multiply(a))
elif c == "divide":
    print(divide(a))






















