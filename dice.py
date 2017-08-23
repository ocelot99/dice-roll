import random

def main():
    dice = int(input("Enter number of dice: "))
    sides = int(input("Enter sides on the dice: "))
    notrandom(dice, sides)
    
def notrandom(dice : int, sides : int):
    total = 0
    maxroll = (sides * dice)
    for x in range(0,dice):
        number = random.randint(1,sides)
        print(x + 1 , ":" , number)
        total = total + number
    print ("sum of all rolls: ", total, "/", maxroll)
    main()

main()
