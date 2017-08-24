import random
import math

def main():
    try:
        dice = int(input("Enter number of dice: "))
        if dice == 0:
            print("Please enter a number higher than 0:")
            main()
        sides = int(input("Enter sides on the dice: "))
        if sides == 0:
            print("Please enter a number higher than 0:")
            main()
        notrandom(dice, sides)
    except (ValueError):
        print("Invalid Input")
        main()
        
def notrandom(dice : int, sides : int):
    total = 0
    maxroll = (sides * dice)
    lowest = math.inf
    highest = -math.inf
    average = 0
    for x in range(0,dice):
        number = random.randint(1,sides)
        if float(lowest) > int(number):
            lowest = number
        if float(highest) < int(number): 
            highest = number
        print(x + 1 , ":" , number)
        total = total + number
    average = (total / dice)
    print ("sum of all rolls: ", total, "/", maxroll)
    print ("average roll: ", average)
    print ("lowest roll: ", lowest)
    print ("Highest roll: ", highest)
    main()

main()
