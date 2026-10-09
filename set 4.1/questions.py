# # 1. Read the first 10 characters, display the pointer position, then reset the pointer to 0 and read again.
# with open("file1.txt","r") as r:
#     print(r.read(12))
#     print(r.tell())
#     r.seek(0)
#     print(r.read(12))
# ================================================ #

# # 2. Read 5 characters, skip to another position using `seek()`, and read the next 10 characters.
# with open("file1.txt","r") as r:
#     print(r.read(5))
#     r.seek(10)
#     print(r.read(10))
# ================================================= #

# #3. Demonstrate what happens when `read()` is called twice without using `seek()`.  
# with open("file1.txt","r") as r:
#     print(r.read(10))
#     print(r.read(10))  # This will read the next 10 characters after the first read 
# =================================================== #

# #4. Display the pointer position after every `readline()` operation.
# with open ("file1.txt","r") as r:
#     print(r.readline())
#     print(r.tell())
#     print(r.readline())
#     print(r.tell())
# ================================================ #

# #5. Read the complete file, reset the pointer using `seek(0)`, and read only the first line.
# with open ("file1.txt","r") as r:
#     print(r.read()) 
#     r.seek(0)
#     print(r.readline())
# ================================================ #

# #6. Create a program that uses `tell()` to report the pointer position before and after reading.
# with open("file1.txt","r") as r:
#     print("Pointer position before reading:", r.tell())
#     content = r.read(15)
#     print("Content read:", content)
#     print("Pointer position after reading:", r.tell())
# =====================================================#

# #7. Read a text file and create another file containing only lines that contain the word `Python`.
# with open("file1.txt","r") as r:
#     with open("file2.txt","w") as w:
#         for line in r:
#             if "python" in line:
#               w.write(line)
#====================================================#

# #8. Read a file and create a second file with all lines converted to uppercase.
# with open("file1.txt","r") as r:
#     with open("file3.txt","w") as w:
#         w.write(r.read().upper())
#=====================================================#

#9. Read a file and write its lines in reverse order to another file.
# with open("file1.txt","r") as f:
#     lines=f.readlines()
#     a=lines[::-1]
#     print(a)
#==========================================================#

#10. Count the frequency of each word in a text file.
# with open("file1.txt","r") as r:
#     text=r.read()
#     words=text.split()
#     frequency={}
#     for word in words:
#         if word in frequency:
#             frequency[word]+=1
#         else:
#             frequency[word]=1
#     for word,count in frequency.items():
#            print(f"{word}:{count}")
# ===============================================================#

# #11 Find the longest line in a file. 
# with open("file1.txt","r") as f:
#     longest_line = ""
#     for line in f:
#         if len(line)>len(longest_line):
#             longest_line=line
#     print("Longest line:",longest_line)
 #===============================================================#

# #12 Find the shortest line in a file.
# with open("file1.txt","r") as f:
#     shortest_line = ""
#     for line in f:
#         if len(line)<len(shortest_line) or shortest_line=="":
#             shortest_line=line
#     print("Shortest line:",shortest_line)
# =============================================================== #

# #13 Remove blank lines from a file and save the result to a new file.
# with open("file1.txt","r") as r:
#     with open("file4.txt","w") as w:
#         for line in r:
#             if line.strip():  # Check if the line is not blank
#                 w.write(line)
#============================================================== #
# # 14Merge two text files into a third file.
# with open("file1.txt","r") as f1:
#     with open("file2.txt","r") as f2:
#         with open("merged_file.txt","w") as mf:
#             mf.write(f1.read())
#             mf.write(f2.read())
# #============================================================== #
# #15. Separate even and odd numbers stored in a file into two different files.
# with open("file1.txt","r") as r:
#     with open("even_numbers.txt","w") as even_file:
#         with open("odd_numbers.txt","w") as odd_file:
#             for line in r:
#                 number = int(line.strip())
#                 if number % 2 == 0:
#                     even_file.write(line)
#                 else:
#                     odd_file.write(line)
#============================================================== #
# # Read a student marks file and calculate average marks.
# with open("marks.txt","r")as r:
#     total_marks=0
#     num_students=0
#     for line in r:
#         total_marks+=int(line.strip())
#         num_students+=1
#     if num_students>0:
#         average_marks=total_marks/num_students
#         print(f"Average marks: {average_marks}")
#     else:
#         print("No students found.")