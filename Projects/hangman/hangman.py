import json
import random

def hangmanGame() -> None:

    file_path:str = 'words.json'
    with open(file_path,'r') as file:
        word_dict:dict = json.load(file)

    word_list:list = word_dict['words']
    chosen_word:str = random.choice(word_list)
    word_display:list = ['_' for _ in chosen_word]
    attempts:int = 8

    while attempts > 0 and '_' in word_display:
        print('\n' + ' '.join(word_display))
        guess:str = input('Guess a letter: ').lower()

        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    word_display[index] = letter
        else:
            print('Nu uh')
            attempts -= 1
    
    if '_' in word_display:
        print('\nYou\'ve lost!')
        print('The word was: ', chosen_word)
        print('Better luck next time')
    else:
        print('\nCongrats ! You did it !')
        print('The word was: ', chosen_word)
        if attempts == 1:
            print('You\'ve had ',attempts,' attempt left')
        else:
            print('You\'ve had ',attempts,' attempts left')


if __name__ == '__main__':
    hangmanGame()