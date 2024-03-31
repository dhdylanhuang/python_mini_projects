import random
import string
from word import words


def get_valid_word(words):
    word = random.choice(words) #randomly chooses something fromt the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed
    
    lives = 6
    
    #getting user input 
    while len(word_letters) > 0 and lives > 0:
        #lives left
        #letters used
        #joins letters ['a', 'b', 'cd'] --> 'a b cd'
        print(f'You have {lives} lives left and have used these letters: ', ' '.join(used_letters))
        
        #what current W - R D is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives -1
                print('Letter is not in word.')
        
        elif user_letter in used_letters:
            print('You have already used this letter. Please try again.')
        else:
            print('Invalid character. Please try again.')
            
    #gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(f'You died, sorry, the word was {word}')
    else:
        print(f'You have guessed the word {word}!!')

print(hangman())