# Write a Python program that performs the following operations on a given string:
#* Convert to uppercase * Convert to lowercase * Swap case
#* Remove leading/trailing spaces * Replace one word with another
#* Split into words * Join the words using a hyphen (`-`)

a=input("enter a string : ")

print(a.upper())
print(a.lower())
print(a.swapcase())
print(a.strip())
print(a.replace("raghav","jeet"))
print(a.split())
print(a.replace(" ","-"))