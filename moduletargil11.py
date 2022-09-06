#3
from Targil11_Class import *
#3.1
Cnumber= int(input("Enter the number of the Course: "))
Cname=input("Enter the name of the Course: ")
Cmax_students= int(input("Enter the max amount of students that can be in the Course: "))
course=Course(Cnumber, Cname, Cmax_students)
#3.2
subject_name= input("Enter the name of the the subjects: ")
professor=input(f"Enter the name of the professor of{subject_name}: ")
while subject_name != "done":
    course.subjects_professor.update({subject_name: professor})
    subject_name = input(f"Enter the name of the the subjects: -if you want to end it enter 'done' ")
    if subject_name == "done":
        break
    professor = input(f"Enter the name of the professor of {subject_name}: ")
#3.3
student_id=int(input("Enter the Student id: "))
while student_id != 0 and len(course.students_in_course)<course.max_amount_of_students:
    student_name=input("Enter the name of the Student: ")
    student_age=int(input("Enter the age of the Student:"))
    student=Student(student_id, student_name, student_age)
    for i in course.subjects_professor:
        student.subjects_grades.update({i:int(input(f"Enter the grade for {student.student_name} in {i}:"))})
    if course.add_studend(student)== False:
        break
    student_id = int(input("Enter the Student id: if you want to end this enter 0"))
#3.4
subject_name=input("Enter a name of a subject you want to do factor on: ")
factor= int(input("Enter the % of the factor you want to give: "))
course.add_factor(subject_name, factor)
#3.5
new_list= course.weak_students()
for i in range(-1, len(new_list)+1, -1):
    course.del_student(course.students_in_course[i])
#3.6
oldest=course.students_in_course()[0].student_age
for student in course.students_in_course():
   if oldest <= student.studend_age:
       oldest=student.studend_age
       oldest_student = student
print(f"The oldest student in the Course is {student}")
#3.7
print(course)
print(student)
