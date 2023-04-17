#coding: utf-8


"""AgePersone = 12
Prix = 15

text = "L'age de Bistrel est de {}, et le prix de la marchandise est de {}£"
print(text.format(AgePersone, Prix))

Nom = input("Enter the player's name\n")

PrixHT = input("Enter the price")

PrixHT = int(PrixHT)

PrixTT = PrixHT + (PrixHT * 2 / 100)
print("Welcome,", Nom,".The PrixTT = ", PrixTT) """

ID = "Bistrel@"
password = "EL157CAPO359"
tryals = 0
print("Enter you ID and Password\n")
while tryals <= 5:
    Identification = input("Enter Your ID address\n")
    PassWord = input("Enter your password\n")
    if ID != Identification and password != PassWord:
        print("Errors")
        tryals += 1
print("Your Account have been block temporaly due to too much attempts!!!")
        if ID == Identification and password == PassWord:
    print("Welcome to your client space\n")



    