''' A college has two clubs:
Science Club = {"Aman","Riya","Rahul","Priya","Ankit"}
Coding Club = {"Rahul","Ankit","Simran","Rohit","Riya"}
Write a Python program to:
1. Display all students enrolled in either club.
2. Display students enrolled in both clubs.
3. Display students only in the Science Club.
4. Display students only in the Coding Club.
5. Check whether the two clubs have any common members.
6. Add a new student to the Coding Club.
7. Remove one student from the Science Club.
8. Print the updated sets.'''

Science_Club = {"Aman","Riya","Rahul","Priya","Ankit"}
Coding_Club = {"Rahul","Ankit","Simran","Rohit","Riya"}

print(Science_Club.union(Coding_Club))
print(Science_Club.difference(Coding_Club))
print(Coding_Club.difference(Science_Club))
print(Science_Club.intersection(Coding_Club))
Coding_Club.add("new_student")
print("coding_club")

