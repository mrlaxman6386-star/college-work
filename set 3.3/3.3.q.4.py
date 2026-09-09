#Write a Python program to check whether a given string is a palindrome or not.
a=input("enter a string : ")

if a[0::1] == a[::-1] :
    print("yes this string is a palindrome")

else :
    print("not a palindrome ")