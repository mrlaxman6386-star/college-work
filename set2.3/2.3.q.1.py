# to print all even & odd numbers separately from 1 to 50 using a loop and conditional statements.

for i in range(1, 51):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")