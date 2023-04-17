#coding: utf-8
calculation = True
month = 12
age = input("Enter his age")
i = 0


try:
    age = int(age)
    print("You have".format(age * month))
except ZeroDivisionError:
    print("The age can't be zero!")
except ValueError:
    print("You have to enter a number")
except:
    print("Value incorrect")
else:
    print("You have made it!")
finally:
    print(("End of Programe..."))
    