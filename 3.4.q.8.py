#Write a Python program to create a dictionary from the following two lists.
#keys = ["ID","Name","Age","City"]
#values = [101,"Ankit",20,"Delhi"]
#Expected Output: {'ID':101,'Name':'Ankit','Age':20,'City':'Delhi’}

keys = ["ID","Name","Age","City"]
values = [101,"Ankit",20,"Delhi"]

item=dict(zip(keys,values))
print(item)
