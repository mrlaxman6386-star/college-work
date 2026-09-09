# wap to only withdraw a cash when the pin is correct or account balance is suffiient.

p=int(input("Enter your password here : "))


if p==123 :
    print("you are welcome")

    a=int(input(" E nter your amount here : "))# a can be defined in if condition 
    if a<100000 :
        print("your amount is receving to you ")

    else :
        print("unavailable balance")#this one is for a

else :
    print("you are entering wrong password ")# this one is for p
