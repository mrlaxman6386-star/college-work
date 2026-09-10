# 15.Write a function get_grade(marks) that returns the grade according to:

# 90–100 → A, 80–89 → B, 70–79 → C, 60–69 → D, Below 60 → F

def get_grade(marks):
    if marks>=90 and marks<=100:
         return "A grade"
    elif marks>=80 and marks<90:
         return "B grade"
    elif marks>=70 and marks<80:
         return "C grade"
    elif marks>=60 and marks<=69:
         return "D grade"
    elif marks<60 :
         return "F grade"

a=int(input("Enter your marks here :"))
print("your garde is : ",get_grade(a))