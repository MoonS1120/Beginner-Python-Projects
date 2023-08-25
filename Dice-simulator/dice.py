from random import randint

def main():
    number_of_dice = int(input("Number of dice: "))

    #Creating a list with 'number_of_dice' numbers of random integer between 1,6 (inclusive)
    for _ in range(number_of_dice):
        dice_numbers.append(randint(1,6))

    horizontal_dice()

    #Totalling
    total = 0
    for number in dice_numbers:
        total += number
    print(f"Total: {total}")


def vertical_dice():
    for i in dice_numbers:
        print('\n'.join(dice_art[i]))


def horizontal_dice():
    for line in range(5):
        for number in dice_numbers:
            print(dice_art.get(number)[line], end='')
        print()

#declaring list
dice_numbers=[]

#ASCII art of dice
dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
        
if __name__ == "__main__":
    main()
