#Electricity Bill: Create a program using functions: get_units(), calculate_bill(),
# display_bill()
# Calculate electricity bill based on units consumed.
def get_unit():
    u=int(input("Enter your units here : "))
    return u
def calculate_bill(u):
    if u>=300:
        return 7*u
    else:
        return 5*u
def display_bill():
    
    b=calculate_bill(u)
    print("Your total unit consumption is :",u)
    print("your total bill amount is :",b)
u=get_unit()
u=display_bill()

