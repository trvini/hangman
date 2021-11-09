from words import wordlist
import random
import string


def get_valid_word(words):
    word = random.choice(wordlist)
    while '-' in word or ' ' in word:
        word = random.choice(wordlist)
    return word


def hangman():
    print("Lets Play Hangman")
    word = get_valid_word(wordlist).upper()
    print(word)
    # letters in the word without repetition
    word_letters = set(word)
    print(word_letters)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()  # letters used by user

    while len(word_letters) > 0:
        #print("you have already used the letters", ' '.join(used_letters))
        user_letter = input("Guess a letter").upper()  # get user input
        print(user_letter)

        # chk if this letter is already used by user
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print("nah!...try again")
            word_list = [letter if letter in used_letters else '-' for letter in word]
            print("current word : ", ' '.join(word_list))
        elif user_letter in used_letters:
            print("hey you already used this letter earlier, guess a new letter ")
        else:
            print("Hey you just typed in an invalid character")


    print("------yippeeee------ you did it")

hangman()

