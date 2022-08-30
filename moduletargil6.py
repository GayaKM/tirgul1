from random import randint
#1
numbersr=[randint(1,100) for i in range(10)]

#2
listen=[1,2,3,4,5,6,7,8,9,10]

#3
newlist=listen[-3:]
print(newlist)
print(f"\n")

#4
print(listen[::-1])
print(f"\n")

#5
for i in range(len(listen)):
    if i%2==0:
        print(listen[i])
print(f"\n")

#6
newlist=listen[:5]
print(listen)
print(f"\n")

#7
newlist=[]
for i in listen:
    if i%2!=0:
        newlist.append(i)
print(newlist)
print(f"\n")

#8
listen = [1,2,3,4,5,6,7,8,9,10]
number = int(input("pleas enter a number kind sir: "))
listen = listen[:7]+[number]+listen[9:]
print(listen)
print(f"\n")

#9
number = int(input("pleas enter a number kind lady: "))
listen = listen[-9:-7]+[number]+listen[-1:]
print(listen)
print(f"\n")

#10
lost=[11, 12, 13, 14, 15, 16, 17]
listi = []
threelist = []
for i in lost:
    if i % 3 != 0:
        listi.append(i)
    else:
        threelist.append(i)
print(f"the new list is {listi} and the numbers that got cut {threelist}")
print(f"\n")

#11
a=1
b=1
buildlist = []
number = int(input("Enter the number for the series: "))
for i in range(number):
    if i == 0:
        buildlist.append(a)
    else:
        buildlist.append(a+b)
        a = b
        b = a+b
print(*buildlist)
print(f"\n")

#12
variant = input("Enter a new string: ")
variant = set(variant)
variant = list(variant)