#Write a Python program to check whether two strings are anagrams.

a=input("enter a string 1 : ")
b=input("entar a string 2 : ")

if sorted(a)==sorted(b) :
    print("yes these are anagrams ")

else :
    print("not a anagrams")
