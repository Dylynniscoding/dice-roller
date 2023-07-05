import random

def roll20():
    roll_result = 0
    for _ in range(1):
        dice = random.randint(1,20)
        roll_result = dice
    if roll_result == 1:
        print("critical fail!")
        return
    if roll_result == 20:
        print("Critical Hit!")
        return

    print(roll_result)
    return
    
    
roll20()