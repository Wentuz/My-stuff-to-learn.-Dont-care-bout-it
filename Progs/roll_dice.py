from random import randint

print("Format xdy, this means 1d20, 1 dice 20 (sides):")

def roll_dice():
    user_input = input()
    tab = user_input.split('d')

    quantity = int(tab[0])
    sides = int(tab[1])
    result = 0

    while quantity != 0:
        result = randint(1, sides) + result
        quantity = quantity - 1
   
    print(result)
    roll_dice()

if __name__ == '__main__':
    roll_dice()