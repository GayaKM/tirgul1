#2
from random import randint
class Bus:
    def __init__(self):
        """Constructor that initialize the attributes of the object"""
        self.seats_in_bus = self.constructor(int(input("Enter the number of seats in the Bus: ")))
        self.number_of_passengers = 0

    def __str__(self):
        """This method will return a string with all the object details that we want to see while print it"""
        return f"The list of the sits in the Bus {self.seats_in_bus} and there is {self.number_of_passengers} pepole on it rigth now "

    def constructor(self, number_of_seats: int):
        """Method that gets the number of seats in the bus and sets a new list filled with 'free'"""
        bus_seats = []
        for i in range(number_of_seats):
            bus_seats.append("free")
        return bus_seats

    def get_on(self, passenger_name: str):
        """Method that get a name of passenger and put hthem in the list if there is free space and changes the number of pepole in the Bus """
        for i in range(len(self.seats_in_bus)):
            if self.seats_in_bus[i] == "free":
                self.seats_in_bus[i] = passenger_name
                self.number_of_passengers += 1
                break
        else:
            print(f"{passenger_name}-There isn't any free seats on the bus, sorry love")

    def get_off(self, passenger_name: str):
        """Method that get a name of passenger and remove them from the list if there is they're there and changes the number of pepole in the Bus """
        for i in range(len(self.seats_in_bus)):
            if self.seats_in_bus[i] == passenger_name:
                self.seats_in_bus[i] = "free"
                self.number_of_passengers -= 1
                break
        else:
            print(f"{passenger_name}-is not even on the bus")

#3
class Loto:
    def __init__(self):
        """Constructor that initialize the attributes of the object"""
        self.random_low = 1
        self.random_up = 45
        self.list_winner = self.wining_list()
        self.max_wining_prise = self.prise_worth()

    def __str__(self):
        """This method will return a string with all the object details that we want to see while print it"""
        return f"The wining combination is {self.list_winner} "

    def wining_list(self):
        """Method that makes list of random 6 numbers in range 1-45 and returns it"""
        new_list = []
        for i in range(6):
            new_list.append(randint(self.random_low, self.random_up))
        return new_list

    def prise_worth(self):
        """This method inputs from the user a max prise and returns it"""
        prise = int(input("Enter the max prise: "))
        return prise

    def guessing(self, number: int):
        """This method returns true if the given number is in the winning list and false if it doesn't """
        if number in self.list_winner:
            return True
        return False

    def how_many_did_you_win(self, solid_guesses: int):
        """Method that get the amount of right guesses and return the value of the prise"""
        if solid_guesses <= 1:
            return 0
        elif 2 <= solid_guesses <= 5:
            return (solid_guesses*self.max_wining_prise)/6
        elif solid_guesses == 6:
            return self.max_wining_prise
        else:
            print("You are cheating")

#1
class Animal:
    def __init__(self, name: str):
        """Constructor that initialize the attributes of the object"""
        self.energy_level = 5.0
        self.hunger_level = 5.0
        self.animal_name = name

    def __str__(self):
        """This method will return a string with all the object details that we want to see while print it"""
        return f" the animal is {self.animal_name}. it's hunger level is: {self.hunger_level} ant it's energy level is: {self.energy_level}"

    def eat(self, food: int):
        """This method gets food in gr and changes the characteristics of the animal by a formula 50gr=hl-1, 100gr=el-1"""
        for i in range(50, food, 50):
            if i != 0 and i % 2 != 0 and self.energy_level > 0:
                self.energy_level -= 1
            elif self.energy_level <= 0:
                self.energy_level = 0
            self.hunger_level -= 1
            if self.hunger_level <= 0:
                self.hunger_level = 0
                print("The animal is full although it didn't ate all it's food")
                break

    def play(self, game: int):
        """This method gets the time of games in minutes and changes the characteristics of the animal by a formula 10 min=hl+2, 10 min=el-2"""
        for i in range(10, game, 10):
            if self.hunger_level <= 8:
                self.hunger_level += 2
            else:
                self.hunger_level = 10
            if self.energy_level >= 2:
                self.energy_level -= 2
            elif self.energy_level == 0:
                print("The game is over cuz the Animal is tired")
                break

    def rest(self, resting: int):
        """This method gets the time of resting in minutes and changes the characteristics of the animal by a formula 30 min=hl+1, 20 min=el+1"""
        for i in range(20, resting, 10):
            if i % 20 == 0 and self.energy_level <= 9:
                self.energy_level += 1
            elif self.energy_level == 10:
                print("The Animal done resting and it would like to play")
                break
            if i % 30 == 0 and self.hunger_level <= 9:
                self.hunger_level +=1
            elif self.hunger_level == 10:
                print("The Animal is done resting and would like to eat")
                break