import random
import logging
import os

logging.basicConfig(
    filename='myProgramLog.txt',
    level=logging.DEBUG,
    format=f' %(asctime)s - %(levelname)s - [{os.path.basename(__file__)[:-3]}] - %(message)s'
)
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower()
    logging.debug(f'First guess: {guess}')
    toss = random.choice(['heads','tails'])
    logging.debug(f'Coin toss: {toss}')
    logging.debug('comparing')
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()
        logging.debug(f'Second guess: {guess}')
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')