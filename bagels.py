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

def find_out(guess):
    if len(guess) != 3:
        sys.exit('invalid guess, must be 3 digits')
    answer = f'{random.randrange(1, 10**3):03}'
    list_ans = list(answer)
    list_guess = list(guess)   

    print(list_ans, list_guess)
    for i in list_guess:
        if i in list_ans:
            print('got it')
guess = input('enter a 3 digit guess: ')
find_out(guess)

def main():


if __name__ == '__main__':
    main()
