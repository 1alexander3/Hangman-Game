import string
import random

WORDLIST_FILENAME = "words.txt"

def load_words():
        print("Loading word list from file...")
        inFile = open(WORDLIST_FILENAME, 'r')
        line = inFile.readline()
        wordlist = line.split()
        print("  ", len(wordlist), "words loaded.")
        return wordlist

def choose_word(wordlist):
        return random.choice(wordlist)


wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    new_str = ''
    for char in secret_word:
        if char in letters_guessed:
            new_str += char
    if new_str == secret_word:
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    new_str = ''
    for char in secret_word:
        if char in letters_guessed:
            new_str += char
        else:
            new_str += '_ '
    return new_str


def get_available_letters(letters_guessed):
    new_str = string.ascii_lowercase
    for char in letters_guessed:
        if char in new_str:
            new_str = new_str.replace(char, '')
    return new_str

def match_with_gaps(my_word, other_word):
    match_letters = []
    match_result = []
    matched = False
    my_word = my_word.replace(' ', '')

    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
                char = my_word[i]
                if str.isalpha(char) is True:
                    match_result.append(char == other_word[i])
                    if char == other_word[i]:
                         match_letters.append(other_word[i])
        for i in range(len(my_word)):
            char = my_word[i]
            if str.isalpha(char) == False:
                match_result.append(other_word[i] not in match_letters)
        if False not in match_result:
            matched = True
    return matched


def show_possible_matches(my_word):
    possible_matches = str()
    
    for word in wordlist:
        if match_with_gaps(my_word, word) == True:
            possible_matches += word + ' '
        
    if possible_matches == '':
        print('No matches found')
    else:
        return possible_matches

def hangman_with_hints(secret_word):
    warnings_left = 3
    guesses = 6

    vowels = 'aeiou'
    letters_guessed = []
    my_word = str(letters_guessed)
    print('Welcome to the game Hangman!\nI am thinking of a word that is', len(secret_word), 'letters long.''\n-------------')
    print('You have', guesses, 'guesses left.''\nAvailable letters:', get_available_letters(letters_guessed))


    word_guessed = is_word_guessed(secret_word, letters_guessed)
    possible_matches = show_possible_matches(my_word)

    while word_guessed == False:
        letter = input('Please guess a letter:')
        letter = letter.lower()


        if letter.isalpha() is False or letter in letters_guessed:
            if letter == '*':
                print('Possible word matches are: ', possible_matches)
            elif warnings_left > 0:
                warnings_left -= 1
                if letter in letters_guessed:
                    print('Oops! You\'ve already guessed that letter. You now have', warnings_left,'warnings:', get_guessed_word(secret_word, letters_guessed))
                else:
                    print('Oops! That is not a valid letter. You have', warnings_left, 'warnings left: ', get_guessed_word(secret_word, letters_guessed))
            else:
                guesses -= 1
                if letter in letters_guessed:
                    print('Oops! You\'ve already guessed that letter. You now have', warnings_left,'warnings:', get_guessed_word(secret_word, letters_guessed))
                else:
                    print('Oops! That is not a valid letter. You have', warnings_left, 'warnings left: ', get_guessed_word(secret_word, letters_guessed))


        if letter in secret_word and letter not in letters_guessed:
            letters_guessed.append(letter)
            print('Good guess:', get_guessed_word(secret_word, letters_guessed))
        elif letter in vowels and guesses > 1:
            letters_guessed.append(letter)
            guesses -= 2
            print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
        elif letter not in secret_word and letter not in letters_guessed and letter.isalpha() is True:
            letters_guessed.append(letter)
            guesses -= 1
            print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
        
        word_guessed = is_word_guessed(secret_word, letters_guessed)

        if word_guessed == False and guesses > 0:
            print('-------------''\nYou have', guesses, 'guesses left.''\nAvailable letters:', get_available_letters(letters_guessed))
        elif word_guessed == False and guesses <= 0:
            print('Sorry, you ran out of guesses. The word was', secret_word + '.')
            break
        else:
            total_score = guesses * len(secret_word)
            print('Congratulations, you won!''\nYour total score for this game is:', total_score)
            break

if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
