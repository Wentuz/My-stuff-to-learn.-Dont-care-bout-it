import json

def game() -> None:
    
    file_path:str = "questions.json"
    with open(file_path, 'r') as file:
        questions:list = json.load(file)

    score:int = 0

    for question in questions:
        print(question['prompt'])
        for option in question['options']:
            print(option)
        answer:str = str(input("Enter your answer: A, B, C or D\n")).upper()

        if answer not in ['A', 'B', 'C', 'D']:
            answer:str = str(input("Last try... No kidding\nEnter your answer: A, B, C or D\n")).upper()

        if answer == question['answer']:
            print('That\'s a correct answer!\n')
            score += 1
        else:
            print('That\'s not a correct answer...', question['answer'],' was a correct answer')
    
    print(f'You got {score} out of {len(questions)} questions correct')
        
    
if __name__ == '__main__':
    game()