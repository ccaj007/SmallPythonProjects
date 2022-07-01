"""
In Bagels, a deductive logic game, you
must guess a secret three-digit number
based on clues. The game offers one of
the following hints in response to your guess:
“Pico” when your guess has a correct digit in the
wrong place, “Fermi” when your guess has a correct
digit in the correct place, and “Bagels” if your guess
has no correct digits. You have 10 tries to guess the
secret number.
"""

import random
import sys

NUM_DIGITS = 3
MAX_GUESSES = 10

def get_secretNum():
    """Returns a string number made up of NUM_DIGITS unique random digits"""
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'you got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # a correct digit is in the correct place
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # a correct digit is in the incorect place
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' # there is no correct digits at all
    else:
        # sort the clues in alphabetcal order so doesn't give info away
        clues.sort()
        return ' '.join(clues)

def main():
    while True:
        secretNum = get_secretNum()
        print(f'You have {MAX_GUESSES} guesses to get it')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{numGuesses}')
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break   # they're correct so break out of loop
            if numGuesses > MAX_GUESSES:
                print('you ran out of guesses')
                print(f'the answer was {secretNum}')

        print('do you want to play again?')
        if not input('> ').lower().startswith('y'):
            break

if __name__ == '__main__':
    main()
