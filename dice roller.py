import random

def roll_dice(num_dice, dice_type):
    total = 0
    for _ in range(num_dice):
        roll = random.randint(1, dice_type)
        total += roll
    return total

def main():
    while True:
        print("\nPlease enter the number of dice and the type of dice you want to roll.")
        print("For example, to roll 2 six-sided dice, enter '2d6'.")
        print("To exit the program, enter 'exit'.")
        user_input = input("Enter dice roll (or 'exit'): ")

        if user_input.lower() == "exit":
            print("Exiting the program.")
            break

        try:
            num_dice, dice_type = user_input.lower().split('d')
            num_dice = int(num_dice)
            dice_type = int(dice_type)

            modifier = int(input("Enter a modifier (if any): "))

            total = roll_dice(num_dice, dice_type) + modifier

            print("\nRolling {}d{} + {}: {}".format(num_dice, dice_type, modifier, total))
        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == '__main__':
    main()