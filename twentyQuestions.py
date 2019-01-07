'''
Filter a range of 2 numbers

@author: Adams-Developer
'''
import stdio
import random

RANGE = 1000

secret = random.randrange(1, RANGE+1)
stdio.write('I am thinking of a secret number between 1 and ')
stdio.writeln(RANGE)
guess = 0
while guess != secret:
    # Solicit one guess and provide one answer.
    stdio.write('What is your guess? ')
    guess = stdio.readInt()
    if (guess < secret):
        stdio.writeln('Too low')
    elif (guess > secret):
        stdio.writeln('Too high')
    else:
        stdio.writeln('You win!')