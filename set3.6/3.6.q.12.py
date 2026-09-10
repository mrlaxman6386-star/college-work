# 12.Write a function print_table(n) that prints the multiplication table of n.
def table(n):
    for i in range (1,11):
     a=(f"{n}*{i} = {n*i}")
     print(a)


n=int(input("Enter a number: "))
table(n)
