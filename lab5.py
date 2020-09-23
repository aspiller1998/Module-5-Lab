import random

process = True
no = random.randint(0, 20)
chance = 0
name = input("What's your name?\n")
print("Hello " + name + " I will guess a number between 0 and 20.")
print("You have 5 guesses.\n")

while process == True:

    choice = int(input("Guess a number\n"))
    if choice == no:
        print("Good. You guessed it.")
        option = input("Do you want to keep playing " + name + "?" + "\n1.Yes\n2.No\n")
        if option == str(1):
            chance = 0
            pass
        if option == str(2):
            exit()
    elif choice > no:
        print("Too hot!")
        chance = chance + 1

    elif choice < no:
        print("Too cool!")
        chance = chance + 1

    else:
        continue

    if int(chance) == 5:
        print("You've reached 5 attempts.")
        print("\n The number was was " + no)
        exit()