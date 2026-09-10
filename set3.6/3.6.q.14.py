# 14.Write a function count_numbers(numbers) that accepts a list and returns the number
# of: Positive numbers, Negative numbers, Zeros
def count_numbers(numbers):
    positive = 0
    negative = 0
    zero = 0
    for i in (numbers):
        if i > 0:
            positive +=1
        
        elif i< 0:
            negative += 1
           
        else:
            zero += 1

    return positive,negative,zero

a=[int(a)for a in input("Enter your numbers here with space : ").split(" ")]
print("positive numbers is : ",count_numbers(a)[0])
print("negative number is : ",count_numbers(a)[1])
print("zero number is : ",count_numbers(a)[2])
            