'''WAP to validate a user's username and password. If both are correct,
display "Login Successful"; otherwise, display "Invalid Username or
Password.'''

n=(input("enter your user name : "))
if n=="raghav":
    print("welcome please enter your password ")

    p=int(input("enter your password :" ))
    if p==123 :
        print("you are sussecfully login")

    else:
        print("wrong password")

else:
    print("wrong user name")