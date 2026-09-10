# Write a function student_result(marks) that accepts a list of marks and returns:
# Total marks, Average marks, Highest marks, Lowest marks
def student_result(marks):
    total_marks=sum(marks)
    average_marks= total_marks/len(marks)
    highest_marks= max(marks)
    lowest_marks= min(marks)
    return total_marks, average_marks, highest_marks, lowest_marks

marks=[int(marks) for marks in input("Enter your marks here with comma : ").split(",")]

print("total marks :",student_result(marks)[0])
print("average marks :",student_result(marks)[1])
print("highest_marks :",student_result(marks)[2])
print("lowest_marks :",student_result(marks)[3])