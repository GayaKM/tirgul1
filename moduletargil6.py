from random import randint
#1
numbersr=[randint(1,100) for i in range(10)]

#2
listen=[1,2,3,4,5,6,7,8,9,10]

#3
newlist=listen[-3:]
print(newlist)

#4
print(listen[::-1])

#5
for i in range(len(listen)):
    if i%2==0:
        print(listen[i])

#6
newlist=listen[:5]
print(listen)

#7
newlist=[]
for i in listen:
    if i%2!=0:
        newlist+=i
print(newlist)

#8
number=int(input("pleas enter a number kind sir: "))
listen=listen[:7]+number+list[9:]
print(listen)

#9
listen=[1,2,3,4,5,6,7,8,9,10]
number=int(input("pleas enter a number kind sir: "))
listen=listen[-9:-7]+number+list[-1:]
print(listen)

#10
newlist=[]
for i in range(len(listen)):
    if listen[i]%3==0:
        listen=listen[:i]+listen[i+1:]
        newlist+=i
print(listen)
print(newlist)

#11
a=1
b=1
buildlist=[]
for i in range (number):
    if i==0:
        buildlist[i]=a
    else:
        buildlist[i]=a+b
        a=b
        b=a+b

#12
