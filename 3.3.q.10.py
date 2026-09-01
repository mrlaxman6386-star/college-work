#Write a Python program to remove duplicate characters from a string

a=input("enter a sentence : ")
b=""

for character in a:
    if character not in b:
        b += character

print(b)