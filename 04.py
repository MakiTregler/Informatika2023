from random import randint
cislo = int(input("Guess a number"))
hadane_cislo = randint (1, 100)

while hadane_cislo != cislo:
    if cislo < hadane_cislo:
        print(cislo, "is lower than the number you are guessing")
        cislo = int(input("Guess a number"))
    elif cislo > hadane_cislo:
        print(cislo, "is higher than the number you are guessing")
        cislo = int(input("Guess a number"))

print("You guessed it!")