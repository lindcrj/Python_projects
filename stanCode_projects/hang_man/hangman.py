"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    1. get a random word
    2. show ______(depends on the length of the random number)
    3. guess
       right => the letter replace '_'
       wrong => N_TURNS-1
    4. Until N_TURNS = 0 or all '_' are replaced by letters
    5. Hung or WIN ~~~ :-O
    """
    r = random_word()
    word = '_'*len(r)
    print('The word looks like: ' + word)
    print('You have ' + str(N_TURNS) + ' guesses left. ')
    guess(r)


def guess(string):
    """
    1. input guess (make sure is upper & the correct type)
    2. {First Guess}
       if guess is right => show the letter
       if the guess is wrong => print the '_'
    3. {Second+ Guess}
       if guess is right => cut the string before the position + the letter + the string afterwards
       if the guess is wrong => Keep as it is, and N_TURNS-1
    4. Judge the end or not
       if there is no '_' can be find in ans => WIN
       if there is no N_TURNS left, and there is still '_' in ans => HUNG
    """
    ans = ''
    n = N_TURNS
    while True:
        alphabet = input('Your guess: ')  # O
        alphabet = alphabet.upper()
        if alphabet.isalpha():
            if len(alphabet) == 1:
                for i in range(len(string)):
                    j = string[i]  # N, O, T, O, R, ...
                    if len(ans) < len(string):
                        if alphabet == j:  # O = O
                            ans += j
                        else:
                            ans += '_'
                    else:
                        if alphabet == j:
                            ans = ans[:i] + j + ans[i+1:]
                        else:
                            ans = ans
                if alphabet in ans:
                    n += 0
                    if ans.find('_') != -1:
                        print('You are correct!')
                        print('The word looks like: ' + ans)
                        print('You have ' + str(n) + ' guesses left. ')
                    else:
                        print('You are correct!')
                        print('You win!')
                        print('The word was: ' + string)
                        break
                else:
                    n -= 1
                    if n != 0:
                        print('There is no ' + alphabet + '\'s in the word.')
                        print('You have ' + str(n) + ' guesses left. ')
                    else:
                        print('You are completely hung : ( ')
                        break
            else:
                print('illegal format.')
        else:
            print('illegal format.')




def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
