#1.1
a=10
b=5
sum=a+b
print(f"the sum is {sum}") #the user gets a massage about what the sum is
print (f"\n")


#1.2
uname=input("pleas enter your name: ")
uage=int(input("pleas enter your age: "))
uyear=int(input("pleas enter the courrent year: "))
print(f"{uname} you will be 100 years old in { (100-uage)+uyear}")
print (f"\n")

#1.3
num1=int(input("pleas enter a number: "))
num2=int(input("pleas enter a number: "))
print(f"the Sum is: {num1+num2}, the Dual is: {num1*num2}, the Modolo  is: {num1%num2}")
print (f"\n")

#1.4
sallery=int(input("pleas enter your sallery:"))
rise=float(input("pleas enter the prusantage of rais"))
rsallery=sallery+(sallery*rise)/100
print(f"your new sallery is: {rsallery}")
print (f"\n")

#1.5
r=float(input("enter the Radius of a circel:"))
pi=3.14
p=2*pi*r
s=pi*r*r
print(f"the space of the circul is: {s} and the perimeter is: {p}")
print (f"\n")

# just to mess around
s=float(input("pleas enter the corrent amount of money in your bank account in nis: "))
doller= 3.8
print(f"you have {s*doller} doller in your account")
print (f"\n")

#2.1
num=int(input("pleas enter a number of your chossing: "))
if num%2==0:
    print("it's an even number")
else:
    print("it's an odd number")
print(f"\n")

#2.2
num1=int(input("pleas enter a number of your chossing: "))
num2=int(input("pleas enter a number of your chossing: "))
num3=int(input("pleas enter a number of your chossing: "))
if num1==num2==num3:                                             # if num1<num2:
    print("all the numbers are the same")                        #max=num2
elif num1>num2 and num1>num3:                                    #else:
    print(f"The biggest number is number 1 which is: {num1}")    #max=num1
elif num1>num1 and num2>num3:                                    #if num3>max:
    print(f"The biggest number is number 2 which is: {num2}")    #max=num3
else:                                                            #print(max)
    print(f"The biggest number is number 3 which is: {num3}")
print (f"\n")

#2.3
computer=input("enter the amont of computers you have chacked today: ")
if computer=="":
    computer=15
computer=int(computer)
print(f"tommorow you will have to chack {computer*2}, you'll get trought it, I belive in you!")
print (f"\n")

#3.1
num1=int(input("give me a number and give me a number now: "))
num2=int(input("give me a number and give me a number now: "))
s=0
while s==0:
    if num1>num2:
        s=num1
        e=num2
    elif num1<num2:
        s=num2
        e=num1
    else:
        s=0
        num1=int(input("give me a number and give me a number now: "))
        num2=int(input("give me a number and give me a number now: "))
if s%2==0:
    while s<e:
        print(s+2)
        s+=2
else:
    while s<e:
        print(s+3)
        s+=2
print (f"\n")
print("or")
num1=int(input("give me a number and give me a number now: "))
num2=int(input("give me a number and give me a number now: "))
if num1>num2:
    for i in range(num1,num2):
        if i!=num1 and i%2==0:
            print(i)

elif num1<num2:
    for i in range(num2,num1):
        if i!=num2 and i%2==0:
            print(i)
else:
    print("erro, they can't be identical twins")
print (f"\n")

#3.2
num=int(input("Enter a number: "))
for i in range (1,num+1):
    if num%1==0 and i!=num and num>0 or num%1==0 and i!=1 and num>0:
        print("it's not firsti number")
        break
    print("wait for it...")
else:
    print(f"your number {num} is firsti, like you mama")
print (f"\n")

#3.3
from random import randint
r=randint(1,9)
num=int(input("let's see if you are the next Ori Galler, guess the number the computer choose: "))
while num!=r:
    if num>r:
        print("the number youv'e choose is higer then the computers")
    else:
        print("the number youv'e choose is lower then the computers")
    num = int(input("let's see if you are the next Ori Galler, guess the number the computer choose: "))
print(f"you have choosen cureectly the number that the computer choose is: {num} and you are an idiot who just waisted time from your life")
print (f"\n")

#3.4
num=int(input("pleas enter a number between 0-100 include- don't be a dick or i'll send you to an endless loop:"))
while num<0 or num>100:
    print("dickhead")
max=100
min=0
r=randint (min,max)
print("the number the computer thinks you choos is:", r)
s=int(input("if the number is higer then yours enter 1 if the number is lower then yours enter 2 and if the number is your number enter 10:"))
count=1
while s!=10:
    if s==1:
         if max>r:
             max=r+1
         r=randint (min,max)
         count+=1
         print("the number the computer thinks you choos is:", r)
         s=int(input("if the number is higer then yours enter 1 if the number is lower then yours enter 2 and if the number is your number enter 10:"))
         if s==10:
             print("yayyy")
             break
    else:
        if min > r:
            min = r-1
        r = randint(min, max)
        count += 1
        print("the number the computer thinks you choos is:", r)
        s = int(input("if the number is higer then yours enter 1 if the number is lower then yours enter 2 and if the number is your number enter 10:"))
        if s == 10:
            print("yayyy")
            break
print(f"the number you have choose is {r} and it took the computer only {count} tries")
print (f"\n")

#3.5
num=int(input("enter the amount of figers you want you serios will have: "))
fn=0
sn=1
for i in range(num):
    if i==0:
        print(fn)
        continue
    nn=sn+fn
    print(sn)
    fn=sn
    sn=nn

#4.1
num=int(input("enter a number you want to have in the sirios : "))
s=[]
while num!= str():
    s.append(num)
    num = input("enter a number you want to have in the sirios if you don't want more numbers enter a string:")
print (f"the max number is:{max(s)} the min number is: {min(s)} the avarge {sum(s)/len(s)}")
print (f"\n")

#4.3
from random import randint
s=[]
for i in range (10):
    r=randint(1,100) #listr.append(randit(1,100))
    listr+=[r]
print(listr)
print (f"\n")

#4.4
num=int(input("enter a number you want to have in the sirios : "))
s=[]
while num!= "":
    s.append(num)
    num = input("enter a number you want to have in the sirios if you don't want more numbers enter a string:")
num1=int(input("enter a number you want to have in the sirios : "))
d=[]
while num1!= "":
    d.append(num1)
    num = input("enter a number you want to have in the sirios if you don't want more numbers enter a string:")
s=s+d
print(f"{s}\n and the length  of the serios len(s)")
print (f"\n")

#4.5
num=int(input("enter a grade : if you don't have more enter <1 "))
s=[]
counth=0
countl=0
while 1<=num<=100:
    num = int(input("enter a grade : if you don't have more enter <1 "))
    s.append(num)
for i in s:
    if i>=60:
        counth+=1
    else:
        countl+=1
print (f"{countl} grades are failed and {counth} grades are pass")
print (f"\n")

#4.6
s=[1,2,3,4,5,6,7,8,9,10]
d=s[-3:]
print(d)
d=s[::-1]
print(d)
for i in range(len(s)):
    if i%2==0:
        print(s[i])
d=[]
for i in s:
    if i%2!=0:
        d.append(i)
print (d)
d=[]
num1=int(input("enter a number : "))
num2=int(input("enter a number : "))
num3=int(input("enter a number : "))
s=s[:4]+[num1,num2]+s[6:]+[num3]
print(s)
d=[]
for i in s:
    d.append(i*2)
print(d)
d=[]
d=[s[0],s[-1]]
print(d)
print(f"\n")

#4.2
sti=input("enter a string:" )
m=sti[::-1]
print(m)
print(f"\n")

#5.1
name=input("enter your first name, my love: ")
lastname=input ("enter my future last name, hubby/wiffy: ")
age=input("enter your age, suga mama/daddy: ")
city=input("enter your city, not that I care: ")
print(f"your name is {name}{lastname}\n your age is {age}\n the city you live on is {city}")
print(f"\n")

#5.2
name=input("enter your first name, my love: ")
age=input("enter your age, suga mama/daddy: ")
city=input("enter your city, not that I care: ")
print("your name is %s, your age %d, you live in %s"%(str(name),age,str(city)))
print(f"\n")

#5.3
word=input("enter your street, home number, city:")
for letter in word:
    if letter==",":
        word=f"{word[:letter]}+/n+{word[letter+1]}"
print(word)
print(f"\n")

#5.4
word=input("enter a word:")
list1=word.split( )
print(len(word))
print(word[3:7])
for letter in list1:
    if letter=="":
        break
print(word[:letter]*3)
print (word.capitalize())
print(f"\n")

#5.5
word=input("enter a word:")
letter=input("enter a letter: ")
count=0
for i in word:
    if i==letter:
        count+=1
print(count)