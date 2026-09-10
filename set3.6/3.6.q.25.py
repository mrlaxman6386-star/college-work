# Organise a program using functions to:
# Accept student name and marks
# Calculate total
# Calculate average
# Determine grade
# Display result

# Condition: main() should control the complete program, while each individual task
# should be performed by a separate function.

def accept():
    name=input("Enter your name here :")
    yoyo=[]
    for i in range (1,6):
        m=int(input(f"Enter your {i} subject marks here :"))
        yoyo.append(m)
    return yoyo,name
def calc_total(yoyo):
    total=sum(yoyo)
    return total
def calc_average(yoyo):
    marks=sum(yoyo)/5
    return marks
def grade(marks):
    if marks >= 90 and marks <= 100:
        return "A grade"

    elif marks >= 80 and marks < 90:
        return "B grade"

    elif marks >= 70 and marks < 80:
        return "C grade"

    elif marks >= 60 and marks < 70:
        return "D grade"

    elif marks < 60:
        return "Fail"
        
def display(name,total,average,grade):
    
    print("======================RESULT======================")
    print("                                                  ")
    print("Your Name is : ",name)
    print("your Total number is : ",total)
    print("Your average number is : ",average)
    print("Your Grade on the basis on numbers is : ",grade)
    print("                                                  ")
    print("==================================================")
def main():
    yoyo,name = accept()

    total = calc_total(yoyo)

    average = calc_average(yoyo)

    result = grade(average)

    display(name, total, average, result)

main()