import random

print("The range for numbers is 1 to 100")
number:int = (random.randrange(1,101))
print(number)

def game() -> None:
    answer = int(input("Guess the number : "))
    while answer == number :
        print("Congrats ! You guessed")
        break
    else:
        print("nope")
        game()

if __name__ == '__main__':      
    game()