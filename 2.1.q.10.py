'''WAP that performs Addition, Subtraction, Multiplication, or Division based
on the user's choice using if-elif-else.'''

c=input("enter your choice : ")
a=int(input(" Enter your value : "))
b=int(input("Enter your second value here : "))

if c=="addition" or "add":
    print("your answer is : ",a+b)

elif c=="multiply" or "multiplication":
                print("your answer is :",a*b)

elif c=="subtarction" or " minus" or "subtract":
    print("your answer is : ",a-b)

elif c=="division" or " devide":
    print("your answer is : ",a/b)

else:
    print("not defied")