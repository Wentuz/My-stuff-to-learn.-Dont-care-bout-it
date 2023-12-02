import random

print("The range for numbers is 1 to 100")
number = (random.randrange(1,101))
print(number)

def game():
    answer = int(input("Guess the number : "))
    while answer == number :
        print("Congrats ! You guessed")
        break
    else:
        print("nope")
        game()
        
game()