class Course:
    def __init__(self, course_number: int, name: str, number: int, max_students: int):
        """Constructor that initialize the attributes of the object"""
        self.course_number = course_number
        self.course_name = name
        self.number_of_students = number
        self.max_num_of_students = max_students

    def __str__(self):
        """This method will return a string with all the object details that we want to see while print it"""
        return f"The Course is:{self.course_name} and it's number is:{self.course_number}, there is {self.number_of_students} students although the max cappesity is {self.max_num_of_students} "

    def number_of_free_places(self, number_of_students: int, max_num_of_students: int):
        """This method will return the difference between the max number of students and how many students are there"""
        places_left = max_num_of_students-number_of_students
        return places_left

    def add_new_students_to_course(self, new_students: int):
        """This method add the number of students it gets to the coures if it can if it can't it will add as many as it can"""
        if self.number_of_free_places(self.number_of_students, self.max_num_of_students) >= new_students:
            self.number_of_students += new_students
        else:
            self.number_of_students = self.max_num_of_students
            new_students -= self.number_of_free_places(self.number_of_students, self.max_num_of_students)


class Student:
    def __init__(self, id_number, name: str, number: int):
        """Constructor that initialize the attributes of the object"""
        self.id_number = id_number
        self.student_name = name
        self.student_grade = number

    def __str__(self):
        """This method will return a string with all the object details that we want to see while print it"""
        return f"The name of the student is:{self.student_name} and their ID number is:{self.id_number},their grade is: {self.student_grade}"

    def checkpass(self):
        """This method returns true if the grade is >= 70 and false if it doesn't"""
        if 70 <= self.student_grade <= 100:
            return True
        return False

    def upgrade(self, pactor: int):
        """This method upgrade the grade times himself and the pactor paresntage"""
        if self.student_grade*(1+pactor/100) <= 100:
            self.student_grade = self.student_grade*(1+pactor/100)
        else:
            self.student_grade = 100
