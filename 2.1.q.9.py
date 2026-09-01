#Calculate electricity bill using following slabs: Up to 100 units: ₹5/unit,
#101–300 units: ₹7/unit, Above 300 units: ₹10/unit

a=int(input("enter your units here : "))

if a<=100 :
    print("your amount is : ",a*5)

elif a>=101 and a<=300 :
    print("your amount is : ",a*7)

elif a>300 :
    print("your amount is : ",a*10)
    