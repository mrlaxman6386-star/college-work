#Write a Python program to check whether a given key exists in a dictionary.
#Example: Input Key: Name Output: Key Found
#Otherwise display: Key Not Found

a={"s1":"raghav","s2":"jeet","s3":"kushagra"}
b=input("enter a key valuue : ")

if b=="s1" :
    print("key found")
    print("your key value is",a["s1"]) 

elif b=="s2":
    print("key found")
    print("yor key value is",a["s2"])

elif b=="s3":
    print("key found")
    print("your key value is",a["s3"])
    
else :
    print("key not find")
