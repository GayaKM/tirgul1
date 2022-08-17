#1
digit=int(input("pleas enter a 3 digits number: "))
while 100<=digit<1000:
    print(f"the sum of the digits is: {digit//100+digit//10%10+digit%10}")
    digit = int(input("pleas enter a 3 digits number: (if you want to finish the loop enter a number that isn't 3 digit length"))
print("erro, you are a disapointment")
print (f"\n")

#2
age=int(input("enter an age: "))
while 0<=age<=120:
    if 0 <= age <= 18:
        print("you are a child- kill yourself")
    elif 19 <= age <= 60:
        print("you are a adult- I fell sorry for you")
    elif 61 <= age <= 120:
        print("you are a senior- you about to die")
    age = int(input("enter an age: "))
print("you are dead")
print("live with it...")
print (f"\n")

#3
num1=int(input("if we are ment to be you'll know what to enter: "))
num2=int(input("pleas enter a number that discribes you as a person: "))
count=1
while num1%2==0 and num2%2==0:
    print (f"the sum is: {num1+num2}")
    count+=1
    num1 = int(input("be my zugi, bring it in: "))
    num2 = int(input("i know you know i know what you need to do: "))
print(f"the dual is:{num1*num2} and we'll see how good you are")
while count>0:
    print("num")
    count-=1
print (f"\n")

#4
while (num1+num2)==10:
    count+=1
    num1 = int(input("enter a number senior/a: "))
    num2 = int(input("enter a number senior/a: "))
print(f"you have reached 10 {count} times. in other words...\n you sick sick person")
print (f"\n")

#5
num1 = int(input("enter a 2 digit number cutie: "))
while 10<=num1<100:
    if 10 <= num1 < 100:
        if (num1 // 10) == 7 or (num1 % 10) == 7 or (num1 % 7) == 0:
            print("you lucky devil it's a lucky number!")
    num1 = int(input("enter a 2 digit number cutie: "))
print("sorry cuite you are out of luck, now you must die")
print (f"\n")