#1
countnum=0
for i in (6):
    num=int(input(" Enter a number my Queen: "))
    countnum+=num
print(f"the avearge is: {countnum/6} but there is nothing avarge about you")
print (f"\n")

#2
countnum=0
ccountzugi=0
for i in (6):
    num=int(input(" Enter a number my Lord: "))
    if num%2==0:
        countnum+=num
        countzugi+=1
print(f"the avearge of your even numbers is: {countnum/countzugi} and as we all know it's even better to be even")
print (f"\n")

#3
for i in (17,99,10):
    print(f"{i} \n BOOM!")
print (f"\n")

#4
countnum=0
for i in (10,99,10):
    countnum+=i
print(f"if you add all the zero's numbers with two digits you'll get {countnum} but it won't change the fact you are a zero ")
print (f"\n")

#5
countnum=0
ccountzugi=0
grade=int(input("Let's see your value: enter your grade"))
while 0<=grade<=100:
    if grade>=60:
        countnum+=grade
        ccountzugi+=1
print(f"{ccountzugi} students have passed away in thier sleep and the averge of your passing tests is {countnum/ccountzugi}")
print (f"\n")

#6
countnum=0
ccountzugi=0
countnom=0
countsingler=0
grade=int(input("Let's see your value: enter your grade"))
while 0<=grade<=100:
    if grade>=60:
        countnum+=grade
        ccountzugi+=1
    else:
        countnom+=grade
        countsingler+=1
print(f"you have {ccountzugi} smart students and thier averge is: {countnum/ccountzugi} and you have {countsingler} stuiped students and thier averge is: {countnom/countsingler}")
print (f"\n")

#7
countnum=0
for i in range (5):
    num = int(input(" Enter a number you highness: "))
    countnum+=num%10
print(f"rigth it's all that matters so the sum of your rigth digits is {countnum} and if you leftwing die in hell")
print (f"\n")

#8
num = int(input(" pleas enter a number: be a friend "))
for i in range(1,num+1):
    if i%5==0:
        print(i)
print("i5")
print (f"\n")

#9
num = int(input(" pleas enter a number: be a really cool person "))
for i in range(2,num+1,2):
    print(i)
print ("i 2 u")
print (f"\n")

#10
num = int(input(" pleas enter a number: don't be mean "))
countnum=0
while num != 0:
    if num%7==0 or num%3==0:
        countnum+=1
print(f" you have {countnum} of your realy wired requsted numbers, pretty random dude...")
print (f"\n")

#1.2
grade=int(input("Let's see your value: enter your grade"))
countnum=0
grades=0
max=0
while 0<=grade<=100:
    grades+=grade
    countnum+=1
    if max<grade:
        max=grade
print(f"the highset grade is: {max}\n the avarge is: {grades/countnum}\n and the diffrence between the highest grade and the avarge is:{grades-(grades/countnum)}")
print (f"\n")

#2.2
p=input("pleas enter a password:")
for i in range(5):
    ip=input("pleas enter the same password again: ")
    if ip==p:
        print("it's correct, the password is safe")
        break
else:
    print("too many tries, your password is not safe")
print (f"\n")

#3.2
num=int(input("pleas enter a number: "))
countnum=0
while num//10!=0:
    countnum+=num%10
    num=num//10
countnum+=num
print(f"the sum of the digits is: {countnum}")
print (f"\n")

#2.4
num=int(input("pleas enter a number: "))
countnum=0
while num//10!=0:
    countnum+=1
    num=num//10
countnum+=1
print(f"the number has {countnum} digits")
print (f"\n")

#3.4
num=int(input("pleas enter a number: "))
min=0
while num!=0:
    if num>0 and num<min:
        min=num
    num = int(input("pleas enter a number: "))
print(f"the smallest and still positiv number that has been entered is: {min}")
print (f"\n")

#4.4
num=int(input("pleas enter a number: "))
while num//10!=0:
    num = num // 10
print(f"the leftest number is: {num}")
print (f"\n")

#5.4
max=0
countnum=0
for i in range (7):
    num = int(input("pleas enter a number: "))
    if max<num:
        max=num
        countnum=i+1
print(f"the highest number was {max} and it was entered in the {countnum} run")
print (f"\n")

#6.4
num = int(input("pleas enter a number: "))
on=0
while num//10!=0:
    on+=(num%10)
    on*=10
    num=num//10
on+=num
print(f"the oppisit number is: {op} and it's dual in 2 is: {op*2}")
print (f"\n")

#7.4
num1 = int(input("pleas enter a number: "))
num2 = int(input("pleas enter a number: "))
while num1<=num2:
    num1 = int(input("pleas enter a number: "))
countnum=0
while num1>num2:
    num1-=num2
    countnum+=1
print(f"the mana is: {countnum} and the sharit is: {num2}")
print (f"\n")

#8.4
min=0
for i in range(5):
    num=int(input("Enter a number: "))
    for i in range (1,num+1):
        if num%1==0 and i!=num  or num%1==0 and i!=1:
          continue
    else:
        num<min
        min=num
print(min)