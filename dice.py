#made by ocelot
#23/08
import random
import math

def main():#I/O
    try:
        dice = int(input("Enter number of dice: "))#Gets number of dice.
        sides = int(input("Enter sides on the dice: "))#Gets number of sides for dice.
        if (sides <= 0 or dice <= 0):
            print("Please enter a number higher than 0:")
            main()
        notrandom(dice, sides)#Passes variables to the dice roll function.
    except (ValueError):
        print("Invalid Input")
        main()
        
def notrandom(dice : int, sides : int):#Rolls the dice.
    total = 0#Initializing some variables.
    maxroll = (sides * dice)
    lowest = math.inf
    highest = -math.inf
    average = 0
    for x in range(0,dice):#Loops the dice roll code for each dice.
        number = random.randint(1,sides)
        if float(lowest) > int(number):#This if statement calculates the lowest roll.
            lowest = number
        if float(highest) < int(number):#This statement calculates the highest roll.
            highest = number
        print(x + 1 , ":" , number)#Displays the result of each roll.
        total = total + number
    average = (total / dice)#Calculates average roll.
    print ("Sum of all rolls: ", total, "/", maxroll)#This section prints out the roll and roll data.
    print ("Average roll: ", average)
    print ("Lowest roll: ", lowest)
    print ("Highest roll: ", highest)
    main()#Loops back to the start

main()
