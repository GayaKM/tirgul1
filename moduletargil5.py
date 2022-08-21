from random import randint
#1
word=input("pleas enter a sentance: ")
for i in word:
    if i=='a':
        word=word[:word.index(i)]+word[word.index(i)+1:]
print(word)
print(f"\n")

#2
word=input("pleas enter a sentance: ")
for i in range(len(word)):
    print(word[0]+word[-1])
print(f"\n")

#3
word=input("pleas enter a sentance: ")
letter=input("enter a letter you like: ")
count=0
for i in word:
    count+=1
    if i==letter:
        print(count-1)
        break
else:
    print(-1)
print(f"\n")

#4
word=input("pleas enter a word: ")
count=0
for i in word:
    count+=1
print(count)
print(f"\n")

#5
word=input("pleas enter a sentance: ")
letter=input("enter a letter you like: ")
count=0
for i in word:
    if i==letter:
        count += 1
print(count)
print(f"\n")

#6
word=input("pleas enter a word: ")
print(word[0].upper()+word[1:])
print(f"\n")

#7
word=input("pleas enter a word: ")
wort=""
for i in word:
    wort+=i+i
print (wort)
print(f"\n")

#8
word=input("pleas enter a word: ")
for i in word:
    if word.count(i)>1:
        print(i)
print(f"\n")

#9
word1=input("pleas enter a word: ")
word2=input("pleas enter a word: ")
count=0
for i in word:
    if word2.find(i):
        count+=1
print(count)
print(f"\n")

#10
name=str(input("enter your name: "))
password=[]
for i in range(6):
    r= int(randint(0,len(name)))
    password+=name[r]
print(password)
print(f"\n")

#11
santence=input("pleas enter a santace: ")
word=input("pleas enter a word: ")
count=0
listind=[]
for i in range (len(santence)):
    for j in word:
        if j==santence[i]:
            count+=1
            listind+=i
            continue
    if count!=len(word):
        listind=[]
    count=0
print(listind)
print(f"\n")

#12
santence=str(input("pleas enter a santace: "))
for i in santence:
    if santence.index(i)==0:
        santence[0]=santence[0].upper()
    elif i=="":
        santence[santence.index(i)+1] = santence[santence.index(i)+1].upper()
print(santence)
print(f"\n")

#13
santence=str(input("pleas enter a santace: "))
letter=str(input("pleas enter a letter: "))
for i in range(len(santence)):
    if santence[i]==letter:
        santence[i]=i.upper()
print(santence)
print(f"\n")