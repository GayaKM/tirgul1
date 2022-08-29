#1
from Targil8_Classes import Course
cnum = int(input("Enter the number of the Course: "))
cname = input("Enter the name of the Course: ")
snum = int(input("Enter the number of students in that Course: "))
mstudents = int(input("Enter the max number of students in that Course: "))
current_course = Course(cnum, cname, snum, mstudents)
print(current_course)
nstudents = int(input("Enter how many new students want to get in to the Course: "))
current_course.add_new_students_to_course(nstudents)
print(current_course)
print(f"\n")

#2
from Targil8_Classes import Student
sid = input("Enter the student ID: ")
sname = input("Enter the name of the student: ")
sgrade = int(input("Enter the student grade: "))
this_student = Student(sid, sname, sgrade)
print(this_student)
if this_student.checkpass():
    print(f"{sname} has passed the test with the grade {sgrade}")
else:
    print(f"{sname} has failed the test with the grade {sgrade}")
pactor = int(input("Enter the present of pactor to the test: "))
this_student.upgrade(pactor)
print(this_student)
print(f"\n")

#3
from Targil8_Classes import Person
pname = input("Enter the Person name: ")
page = int(input("Enter the person age: "))
num_of_kids = int(input("Enter the number of kids this person has: "))
persy= Person(pname, page, num_of_kids)
print(persy)
if persy.haschildren():
    print(f"The person has {persy.number_of_kids} kids")
else:
    print(f"The person is happy, they have no kids")
print(f"The person is: {persy.agegroup()}")
print(f"\n")

#4
from Targil8_Classes import Hard_Disk
disk_size = int(input("Enter the size of the disk: "))
on_key = Hard_Disk(disk_size)
print(on_key)
nfname = input("Enter a name of file:")
nfsize = int(input("Enter the file size: "))
if on_key.add_file(nfname, nfsize):
    print(on_key.file_list)
if on_key.del_file(nfname):
    print(on_key)
nfname = input("Enter a name of file:")
nfsize = int(input("Enter the file size: "))
if on_key.update_file(nfname, nfsize):
    print(on_key)
print(f"\n")