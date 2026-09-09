#Write a Python program to remove: * specific key * last inserted item
#Display the dictionary after each operation.
a={"1":"python","2":"java","3":"html"}
b={"4":"css"}
a.pop("1")
a.update(b)
a.popitem()
print(a)