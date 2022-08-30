# 1
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
        places_left = max_num_of_students - number_of_students
        return places_left

    def add_new_students_to_course(self, new_students: int):
        """This method add the number of students it gets to the coures if it can if it can't it will add as many as it can"""
        if self.number_of_free_places(self.number_of_students, self.max_num_of_students) >= new_students:
            self.number_of_students += new_students
        else:
            self.number_of_students = self.max_num_of_students
            new_students -= self.number_of_free_places(self.number_of_students, self.max_num_of_students)


# 2
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
        if self.student_grade * (1 + pactor / 100) <= 100:
            self.student_grade = self.student_grade * (1 + pactor / 100)
        else:
            self.student_grade = 100


# 3
class Person:
    def __init__(self, name: str, age: int, number: int):
        """Constructor that initialize the attributes of the object"""
        self.person_name = name
        self.person_age = age
        self.number_of_kids = number

    def __str__(self):
        """This method will return a string with all the object details that we want to see while print it"""
        return f"The name of the person is {self.person_name} , their age is {self.person_age} years old. and {self.number_of_kids} kids"

    def haschildren(self):
        """This method returns true if the person has kids and false if there isn't"""
        if self.number_of_kids == 0:
            return False
        return True

    def agegroup(self):
        """This method returns a massage about the age group of the person """
        if 0 <= self.person_age <= 18:
            return f"You are a Child"
        elif 19 <= self.person_age <= 60:
            return f"You are an Adult"
        elif 61 <= self.person_age <= 120:
            return f"You are a Senior"
        else:
            return f"You are Dead"


# 4
class Hard_Disk:
    def __init__(self, disk_size: int):
        """Constructor that initialize the attributes of the object"""
        self.disk_size = disk_size
        self.file_list = dict({})

    def __str__(self):
        """This method will return a string with all the object details that we want to see while print it"""
        return f"The size of the hard disk is {self.disk_size} , the list pf the file is {self.file_list}"

    def used_space(self):
        """This method will bring the sum of the used space on the disk"""
        new_list = list(self.file_list.values())
        return sum(new_list)

    def free_space(self):
        """This method will bring how much free space there is in the disk"""
        return int(self.disk_size - self.used_space())

    def add_file(self, file_name: str, file_size: int):
        """This method will return true if the list of the files was updated"""
        if int(self.free_space()) >= file_size:
            if file_name in self.file_list:
                print("the name already exists so it doesn't go in")
                return False
            else:
                self.file_list.update({file_name: file_size}) #self.file_list[file_name] = file_size
                return True
        else:
            print("There is not enough room un the Hard disk ")
            return False

    def del_file(self, file_name: str):
        """This method gets a file name and if it in the file list it delete it and returns true else false"""
        if file_name in self.file_list:
            del self.file_list[file_name]
            return True
        else:
            return False

    def update_file(self, file_name: str, new_size: int):
        """This method gets new size and name of already existed file and update it. returns true if it did and false if it didn"t """
        if file_name in self.file_list:
            current_file_size=self.file_list[file_name]
            if self.free_space()+current_file_size > new_size:
                self.file_list[file_name] = new_size
                return True
        else:
            print("There is not such file")
            return False
