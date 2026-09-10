# Create the following functions:

# get_number()
# square()
# cube()
# display()

# get_number() should provide a number to square() and cube(), and display() should
# display the results.
def get_number():
    n=int(input("Enter a number here :"))
    return n
def square(n):
    return n*n
def cube(n):
    return n*(n*n)
def display(n):
    a=square(n)
    b=cube(n)
    print("=========================")
    print("Square of a number is : ",a)
    print("Cube of a number is : ",b)
    print("==========================")
a=get_number()
display(a)
