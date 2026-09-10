# Convert this program into functions
# Given: name = input("Enter name: ")

# marks = []
# for i in range(5):

# marks.append(int(input("Enter marks: ")))

# total = sum(marks)
# average = total / 5
# if average >= 40:

# result = "Pass"

# else:

# result = "Fail"
# print("Name:", name)
# print("Total:", total)
# print("Average:", average)
# print("Result:", result)

# Task: Divide this program into at least 4 meaningful functions.
def enter_name_marks():
    name = input("Enter name: ")
    marks = []
    
    for i in range(5):
         marks.append(int(input("Enter marks: ")))
    return name,marks
def total(marks):
    total = sum(marks)
    return total
def average(total):
    average = total / 5
    if average >= 40:
        result = "Pass"
    else:
        result = "Fail"

    return average,result

def display(name,total,average,result):

      print("Name:", name)
      print("Total:", total)
      print("Average:", average)
      print("Result:", result)

name, marks = enter_name_marks()
total_marks = total(marks)
avg, result = average(total_marks)
display(name, total_marks, avg, result)