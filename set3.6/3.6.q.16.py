# Student Marks Program: Create a program using separate functions: input_marks(),
# calculate_total(), calculate_average(), display_result()
# Program should accept marks of 5 subjects & display total, average and result.
def input_marks():
    marks = []

    for i in range (1,6):
        a=int(input(f"Enter your {i} subject number hare : "))
        marks.append(a)
    return marks
def calculate_total(marks):
    s=sum(marks)
    return s
def calculate_average(marks):
    e=sum(marks)/len(marks)
    return e
def display_result(marks):
    s=calculate_total(marks)
    e=calculate_average(marks)
    print("total :",marks)
    print("sum :",s)
    print("average :",e)

marks = input_marks()
display_result(marks)

