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

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        
        print("You have", lives, "lives and you have used these letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]

        print("The current word is: ", " ".join(word_list))


        guess = input("Guess a letter: ").upper()
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                lives -= 1

        elif guess in used_letters:
            print("You have already used this letter. Please try again.")
        
        else:
            print("You have entered an invalid character. Please try again.")
    
    if lives == 0:
        print("You lose! The word was:", word)
    else:
        print("You win!")
        
    
            
            



hangman()