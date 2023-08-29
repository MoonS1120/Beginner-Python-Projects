from random import randint

def main():
    num_dice = int(input("Number of dice: "))
    dice_val = roll_dice(num_dice)

    horizontal_dice(dice_val)

    total = 0
    for number in dice_val:
        total += number
    print(f"Total: {total}")

def roll_dice(num_dice):
    dice_val = [randint(1,6) for _ in range(num_dice)]
    return dice_val

def vertical_dice(dice_val):
    for i in dice_val:
        print('\n'.join(dice_art[i]))

def horizontal_dice(dice_val):
    for line in range(5):
        for num in dice_val:
            print(dice_art[num-1][line], end='')
        print()

dice_art = [
       [
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
       ],
       [
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
       ],
       [
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
       ],
       [
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
       ],
       [
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
       ],
       [
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
       ]
]

if __name__ == "__main__":
    main()