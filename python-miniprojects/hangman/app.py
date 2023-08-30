from wordbank import words
import random
import string

'''
select random word
create hangman


'''

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #set of letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #set of guessed letters

    while len(word_letters) > 0:
        

        guess = input("Guess a letter: ").upper()
        if guess in word_letters:
            pass



hangman()