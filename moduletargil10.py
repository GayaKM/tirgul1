#2
from Targil10_Classes import Bus
schooly = Bus()
activity = int(input("Enter 1 if you want to get somebody on the bus\nEnter 2 if you want to get somebody off the bus\nEnter 0 if you want to end this:"))
count = 0
while activity != 0:
    count += 1
    if activity == 1:
        schooly.get_on(input("Enter the name of the passenger that will get on the bus: "))
    elif activity == 2:
        schooly.get_off(input("Enter the name of the passenger that will get off the bus: "))
    else:
        for i in range(count):
            print(end="num")
    activity = int(input("Enter 1 if you want to get somebody on the bus\nEnter 2 if you want to get somebody off the bus\nEnter 0 if you want to end this:"))
print(schooly)
print(f"\n")

#3
from Targil10_Classes import Loto
toto = Loto()
print(toto)
count = 0
for i in range(6):
    guess = int(input("Enter a guess between 1-45: "))
    if 1 > guess or guess > 45:
        print("You are out cuz you ain't following the rules")
        print("you have won 0")
        break
    if toto.guessing(guess):
        count += 1
else:
    print(f"You have won: {toto.how_many_did_you_win(count)}")
print(f"\n")

#1
from Targil10_Classes import Animal
name = input("Enter the name of the Animal:")
haia = Animal(name)
activity = int(input("Enter 1 if you want to feed the Animal\nEnter 2 if you want to play with the Animal\nEnter 3 if you want the Animal to rest\nEnter 0 if you want to end this:"))
count = 0
while activity != 0:
    count += 1
    if activity == 1:
        haia.eat(int(input("Enter the amount of food you give to the Animal in gr: ")))
        print(haia)
    elif activity == 2:
        haia.play(int(input("Enter the time in minutes that you play with the Animal: ")))
        print(haia)
    elif activity == 3:
        haia.rest(int(input("Enter the time in minutes that the Animal rest: ")))
        print(haia)
    else:
        for i in range(count):
            print(end="ahwembawah")
    activity = int(input("Enter 1 if you want to feed the Animal\nEnter 2 if you want to play with the Animal\nEnter 3 if you want the Animal to rest\nEnter 0 if you want to end this:"))
