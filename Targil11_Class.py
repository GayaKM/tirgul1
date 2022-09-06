class Student:
    def __init__(self, sid, sname, sage):
        self.student_id = sid
        self.student_name= sname
        self.studend_age= sage
        self.subjects_grades= dict({})

    def __str__(self):
        return f"the student id is {self.student_id} and thier name is {self.student_name} and his age is:{self.studend_age}" \
               f"heres a list of the subjects and the grades of the students{self.subjects_grades}"

    def add_grade(self, subject_name, grade):
        """Method that gets a subjects name and a grade and add it to the subjects_grades dictionry"""
        self.subjects_grades[subject_name] = grade

    def calc_factor(self, subject_name, factor):
        """Method that gets factor% and subject name and update the grade by thr factor"""
        value = self.subjects_grades[subject_name]
        if value + (factor/100)* value <= 100:
            self.subjects_grades[subject_name] = value + (factor/100)* value
        else:
            self.subjects_grades[subject_name] = 100

    def average(self):
        """Method that returns the average of the grades from the dictionry """
        values = list(self.subjects_grades.values())
        return sum(values) / len(self.subjects_grades)

    def __eq__(self, other):
        """Method that returns true if the id of two studens are the same"""
        if self.student_id == other.student.id:
            return True
        else:
            return False

    def __gt__(self, other):
        """Method that returs true if the age of the first studend is bigger then the other"""
        if self.studend_age > other.student_age:
            return True
        else:
            return False

class Course:
    def __init__(self, cnumber, cname, max_students):
        self.course_number = cnumber
        self.course_name = cname
        self.subjects_professor= dict({})
        self.students_in_course= []
        self.max_amount_of_students= max_students

    def __str__(self):
        return f"Cours{self.course_name},number{self.course_number} can have {self.max_amount_of_students} students" \
               f"heres a list of the students in the course {self.students_in_course} and the pro and their subjects {self.subjects_professor}"

    def add_studend(self, student:Student):
        """Method that gets a student and adds it to the list if it possable and returns true if it did else"""
        if len(self.students_in_course) < self.max_amount_of_students:
            self.students_in_course.append(student)
            return True
        else:
            return False

    def add_factor(self, subject_name, factor):
        """Method gets subject name and factor% and goes over the list of students in the course and changes thier grades"""
        for i in range( len(self.students_in_course)):
            self.students_in_course[i].calc_factor(subject_name, factor)

    def del_student(self, student:Student):
        """gets a students and delete it from the course"""
        if student in self.students_in_course:
            self.students_in_course.remove(student)

    def averages(self):
        """Method that returns a list of the avergaes of the students"""
        new_list=[]
        for student in self.students_in_course:
            new_list.append(student.average())
        return new_list

    def weak_students(self):
        """Method that return a list of the lowest averge index in the student in the Course"""
        list1=self.averages()
        mini=min(list1)
        listmin= []
        for i in range(len(list1)):
            if mini == list1[i]:
                listmin+=i
        return listmin
