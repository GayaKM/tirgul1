#1
num1=int(input("pleas enter a number of your chossing: "))
num2=int(input("pleas enter a number of your chossing: "))
if (num1+num2)%2==0:
    print("it's an even number")
else:
    print("it's an odd number")
print (f"\n")

#2
num= int(input("pleas enter a 3 digit number: "))
if 100<=num<1000:
   print(f"the sum of the digits is: {num//100+num%10+num//10%10}")
else:
    print("erro")
print (f"\n")

#3
age=int(input("enter your age: "))
if 0<=age<=18:
    print("you are a child")
elif 19<=age<=60:
    print("you are a adult")
elif 61<=age<=120:
    print("you are a senior")
print (f"\n")

#4
num1=int(input("pleas enter a number of your chossing: "))
num2=int(input("pleas enter a number of your chossing: "))
if num1%2==0 and num2%2==0:
    print (num1+num2)
else:
    print(num1*num2)
print (f"\n")

#5
num1=int(input("pleas enter a number of your chossing: "))
num2=int(input("pleas enter a number of your chossing: "))
if (num1+num2)==10:
    print("congrts the sum is 10 and so are you!")
else:
    print("it's not a 10 , you loser")
print (f"\n")

#6
grade=int(input("enter the grade:"))
if 0<=grade<=100:
    if grade>=70:
        print("you have passed baby")
    else:
        print("sorry baby you have failed")
else:
    print("erro")
print (f"\n")

#7
num= int(input("pleas enter a 2 digit number: "))
if 10<=num<100:
    if (num//10)==7 or (num%10)==7 or (num%7)==0:
        print("you lucky devil it's a lucky number!")
else:
    print("erro")
print (f"\n")

#8
d=input("enter a day in numbers:")
m=input("enter a month in numbers:")
y=input("enter a year in numbers:")
if d=="" or m=="" or y=="":
    print("it's an erro, you must enter a number. and because you were too lazy and just entered nothing you must do it all again")
    d = input("enter a day in numbers:")
    m = input("enter a month in numbers:")
    y = input("enter a year in numbers:")
d=int(d)
m=int(m)
y=int(y)
if 1<=d<=31 and 1<=m<=12 and 1950<=y<=2020:
   if m==9 and d<=30 or m==11 and d<=30 or m==4 and d<=30 or m==6 and d<=30: # if (m==9 or m==11 or m==4 or m==6) and d<=30
    if (y%100)<10:
        print(f"{d}/{m}/0{y%100}")
        if m < 10:
            print(f"{d}/0{m}/0{y % 100}")
            if d < 10:
                print(f"0{d}/0{m}/0{y % 100}")
        print(f"{d}/{m}/0{y % 100}")
    else:
        print(f"{d}/{m}/{y%100}")
        if m < 10:
            print(f"{d}/0{m}/0{y % 100}")
            if d < 10:
                print(f"0{d}/0{m}/0{y % 100}")
   elif m==2 and d<=28:
       if (y % 100) < 10:
           if m<10:
               print(f"{d}/0{m}/0{y % 100}")
               if d<10:
                   print(f"0{d}/0{m}/0{y % 100}")
           print(f"{d}/{m}/0{y % 100}")
       else:
           print(f"{d}/{m}/{y % 100}")
           if m < 10:
               print(f"{d}/0{m}/0{y % 100}")
               if d < 10:
                   print(f"0{d}/0{m}/0{y % 100}")
   else:
       if (y % 100) < 10:
           print(f"{d}/{m}/0{y % 100}")
           if m < 10:
               print(f"{d}/0{m}/0{y % 100}")
               if d < 10:
                   print(f"0{d}/0{m}/0{y % 100}")
           print(f"{d}/{m}/0{y % 100}")
       else:
           print(f"{d}/{m}/{y % 100}")
           if m < 10:
               print(f"{d}/0{m}/0{y % 100}")
               if d < 10:
                   print(f"0{d}/0{m}/0{y % 100}")
elif 1>d and d>31:
    print("you entered the day incoractly, it's an erro my friend")
elif 1>m and m>12:
    print("you entered the month incoractly, it's an erro my friend")
elif 1950>y and y>2020:
    print("you entered the year incoractly, it's an erro my friend")
print (f"\n")