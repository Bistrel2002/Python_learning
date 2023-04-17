#coding: utf-8

class Human:
    """
    Human's class
    """

    Human_created = 0
    def __init__(self):
        print("Creation of a Humain...")
        self.fname = input("First Name")
        self.lname = input("Last Name")
        self.age = input("Age") 
        self.age = int(self.age)
        self.height = input("Height")
        self.height = float(self.height)
        Human.Human_created += 1 
    def say(self, message):
        self.message = "Hi to everyone"
        print("{} said {}",format(self.lname, self.message))
    
print("Beginning of the project...")

H1 = Human()
print("First Name: {}", format(H1.fname))
print("Last Name: {}", format(H1.lname))
H1.say()
print("Age: {}", format(H1.age), "years old")
print("Heigth: {}", format(H1.height),"cm")


H2 = Human()
print("First Name: {}", format(H2.fname))
print("Last Name: {}", format(H2.lname))
print("Age: {}", format(H2.age), "years old")
print("Heigth: {}", format(H2.height),"cm")

print("Human's created: {}", format(Human.Human_created))




