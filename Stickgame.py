from random import *
instructions = "The aim of the game is to remove stick and trick the computer into removing the last stick."
numStick = 21
turns = randint(0, 1)

def handleInput():
    while True:
        try:
            userInput = int(input("Please enter your move."))
            if userInput > 3 or userInput <= 0:
                print("The input doen't match range requirements.")
            else:
                return userInput
        except: 
            print("Your input is invalid.")

def getComputer(num):
    compute = num % 4
    if compute <= 0:
        return 1
    else:
        return compute

def updateScreen(num):
    print("The current number of sticks are: {sticks}".format(sticks = num))

print(instructions)
while numStick > 0:
    if turns == 0:
        updateScreen(numStick)
        computer = getComputer(numStick)
        print("Computer is removing: {num}".format(num = computer))
        numStick -= computer
        if numStick <= 0:
            print("Player won.")
        else:
            turns = 1
    elif turns == 1:
        updateScreen(numStick)
        user = handleInput()
        numStick -= user
        if numStick <= 0:
            print("Computer won.")
        else:
            turns = 0

    

