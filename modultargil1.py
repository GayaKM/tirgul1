#targil1
num1=5
num2=20
print(f"+:{num1+num2}\n-:{num1-num2}\n*:{num1*num2}\n%:{num1/num2}")
print (f"\n")
print(f"{num1}+{num2}={num1+num2}\n{num1}-{num2}={num1-num2}\n{num1}*{num2}={num1*num2}\n{num1}/{num2}={num1/num2}")
print (f"\n")
num1=int(input("pleas enter a number: "))
num2=int(input("pleas enter a number: "))
print(f"{num1}+{num2}={num1+num2}\n{num1}-{num2}={num1-num2}\n{num1}*{num2}={num1*num2}\n{num1}/{num2}={num1/num2}")
print (f"\n")

#targil4
name=input("what's your name? ")
cyear=int(input("enter the courrent year: "))
age=int(input("what's your age? "))
fyear=int(input("enter the year you want in the futuer: "))
print(f"{name} will be {(fyear-cyear)+age} in year {fyear}")
print (f"\n")

#targil2
d=int(input("pleas enter the day: "))
m=int(input("pleas enter the month: "))
y=int(input("pleas enter the year: "))
print(f"{d}/{m}/{y%100}")
print (f"\n")

#targil 3
hbnum=int(input("enter a three digite number: "))
first=hbnum//100
secound=hbnum//10%10
thired=hbnum%10
print(f"the new number is:{thired*100+secound*10+first}")
print (f"\n")

#trgil 5
digit1=int(input("pleas enter a digit: "))
digit2=int(input("pleas enter a digit: "))
digit3=int(input("pleas enter a digit: "))
print(f"the first number is {digit1*100+digit2*10+digit3} and the secound number is {digit1*200+digit2*20+(digit3*2)} ")
print (f"\n")

#targil 6
number1=int(input("pleas enter a number: "))
number2=int(input("pleas enter a number: "))
print(f"{number1//number2},{number1/number2},{number1%number2}")
print (f"\n")