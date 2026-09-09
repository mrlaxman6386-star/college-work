''' Create the nested dictionary for each department of RDEC. Department should
contain: HOD Name, Number of Faculty, Number of Students
Then write statements to:
1. Print the HOD of the ECE department.
2. Print the number of students in the CSE department.
3. Update the faculty count of the ME department.
4. Add a new department named Civil.
5. Print all department names.
6. Print the complete nested dictionary.'''

RDEC={"cse":{"hod_name":"dr.love dixit","number_of_facuty":"15","number_of_students":"360"},
      "ece":{"hod_name":"dr.xy","number_of_faculty":"8","number_of_student":"40"},
      "me":{"hod_name":"dr.abc","number_of_faculty":"9","number_of_student":"11"}}

print(RDEC["cse"]["hod_name"])
print(RDEC["cse"]["number_of_students"],"")
RDEC["ece"]["number_of_faculty"]=10
b={"civil":{"hod_name":"kbc","number_of_faculty":"5","number_of_students":"15"}}
RDEC.update(b)
print(RDEC)
print(RDEC.keys())
#10
print(["cse"]["number_of_students"])