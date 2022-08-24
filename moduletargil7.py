#1
def sum_digits (num): # Method that brings back the sum of the digits of the number it gets
    sumy=0
    num=int(num)
    while num//10!=0:
        sumy+=num%10
        num=num//10
    sumy+=num
    return sumy

threedigit=int(input("pleas enter a 3 digits number: don't test me ")) # The main program
print(f"the sum of your digits is {sum_digits(threedigit)}")
print (f"\n")

#2
def is_it_three_digits (num): #Method that return True if the number is three digit length else will return False
    if 100<=num<1000:
        return True
    return False

threedigit=int(input("pleas enter a 3 digits number: don't be an ass ")) # The main program
if is_it_three_digits(threedigit):
    print("It's indeed a three digit number")
else:
    print("It's not a three digits number, Asshole")
print(f"\n")

#3
def print_string_for_number (string, num):# Method that print the string it got the number of times from the number it got
    for i in range(num):
        print(string)

number=int(input("Enter a number:"))#the MAIN program
name= input("Enter a name: ")
print_string_for_number(name,number)
print(f"\n")

#4
def from_one_till_you_sum (num):#brings back the sum of the number between 1 to the number it given
    sumy=0
    for i in range(1,num+1):
        sumy+=i
    return sumy

number=int(input("Enter a number: "))#the MAIN program
print(from_one_till_you_sum(number))
print(f"\n")

#5
for i in range(5): #the Main program
    number = int(input("Enter a number: "))
    print(from_one_till_you_sum(number))
print(f"\n")

#6
def print_in_one_row_the_seris (num1,num2): #method that print the numbers between the numbers that were given in a row
    for i in range(num1,num2+1):
        print(end=f"{i}\t")

number1 = int(input("Enter the smaller number: "))#the Main program
number2 = int(input("Enter the larger number: "))
print_in_one_row_the_seris(number1,number2)
print(f"\n")

#7
def the_smaller_number (num1,num2):#method that gets 2 numbers and gives the smallest one
    if num1<num2:
        return num1
    elif num1>num2:
        return num2
    else:
        return num1

def the_larger_number (num1,num2):#method that gets 2 numbers and gives the largest one
    if num1>num2:
        return num1
    elif num1<num2:
        return num2
    else:
        return num1

number1 = int(input("Enter the smaller number: "))#the Main program
number2 = int(input("Enter the larger number: "))
print_in_one_row_the_seris(the_smaller_number(number1,number2),the_larger_number(number1,number2))
print(f"\n")

#8
def power_of_number_and_power(num1,num2): #method that gives the power of one number it gets in the other number it gets
    power=num1
    for i in range(num2-1):
        power*=num1
    return power

number1 = int(input("Enter the number you want to do the action on: "))#the Main program
number2 = int(input("Enter the power of the number: "))
print(power_of_number_and_power(number1,number2))
print(f"\n")

#9
def what_age_group_age_is (age): #Method that gets age and give back the included age group in string
    if 0<=age<=18:
        return "child"
    elif 19<=age<=60:
        return "adult"
    elif 61<=age<=120:
        return "senior"
    else:
        return "you dead hun"

for i in range (5):#the MAIN program
    age=int(input("Enter an age: "))
    print(what_age_group_age_is(age))
print(f"\n")

#10
def do_the_grade_pass (grade): #Method that gets grade and give back true if it pass and false if it dosen't
    if 70<=grade<=100:
        return True
    return False

for i in range(5):#the MAIN program
    grade=int(input("Enter a grade: "))
    if do_the_grade_pass(grade):
        print("You have passed, goog luck in haven")
    else:
        print("You are a failer, your Mom is emberest by you")
print(f"\n")

#11
def list_fourtytow (list1):#Method that makes alist with all the even numbers between 2-40 in an ampty list it gets
   for i in range (2,41,2):
       list1.append(i)
   return list1

newlist=[] #the MAIN program
print(list_fourtytow(newlist))
print(f"\n")

#12
from random import randint
def random_twenty_values_list (list1): #Method that fills an empty list that was given with random 20 values 100-1
    for i in range(20):
        list1.append(randint(1,100))
    return list1

def how_many_times_number_in_list (list1,num): #Method that returns how many times thr given numbers showen in the given list
    count=list1.count(num)
    if count>0:
        return count
    return 0

list1=[] #the MAIN program
list1=random_twenty_values_list(list1)
print(list1)
number=int(input("Enter a number, but ain't yours: "))
print(how_many_times_number_in_list(list1,number))
print(f"\n")

#13
def index_of_the_max_value (string1:str): #Method that return the index of the max value in the given list, if there is more then 2 then it will return a masega
    maxi=max(list1)
    if how_many_times_number_in_list(list1,maxi)==1:
        return string1.index(maxi)
    else:
        return "I know I'm not the only one"

print(index_of_the_max_value(list1)) #the MAIN program
print(f"\n")

#14
def grades_to_the_students (num): #Method that returns a list as long as the number it gets filld with grades from the user
    list1=[]
    for i in range (num):
        list1.append(int(input("Enter a grade, be nice: ")))
    return list1

numstudents=int(input("pleas enter the number of students in the class: ")) #the MAIN program
print(grades_to_the_students(numstudents))
print(f"\n")

#15
def avarge_of_the_list (list1): #Method that get a list and returns the avarge of it
    return sum(list1)/len(list1)

print(avarge_of_the_list(grades_to_the_students(numstudents))) #the main program
print(f"\n")


