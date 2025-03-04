from random import randint

def diceRoll(number,d):
    roll = 0
    for die in range(number):
        roll += randint(1,d)
    print(f"Rolled {number}d{d} for {roll}")
    return roll