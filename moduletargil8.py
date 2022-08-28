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

