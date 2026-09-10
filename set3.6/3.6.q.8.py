# Write a function count_vowels(text) that accepts a string and returns the number of
# vowels in it.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    now = 0
    for char in text:
        if char in vowels:
            count += 1
        elif char.isalpha():
            now += 1
    return count,now 
a=input("Enter your text here : ")  
print("The number of vowels in the text is :",count_vowels(a)[0])
print("The number of consonants in the text is :",count_vowels(a)[1])