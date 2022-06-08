"""A number-guessing game."""

from random import randint

name = input('what is your name >')
print('nice to meet you', name)
print(name,'im thinking of a number between 1-100 can you guess what it is?')

number = randint(1,100)

count = 0

while True:
    
    try:
        guess = input('what is your guess? ')
        guess = int(guess)
    except ValueError:
        print('not a valid number')

    if guess < 1 and guess > 100:
        print('please pick a number between 1-10')
        continue
    
    count += 1 

    if guess < number:
        print('that number is to low, try again')
        continue
    elif guess > number:
        print('that number is to high, try again')
        continue
    else:
        print('that is correct')
        print(name,'you guessed the number in',count, 'attempts')
        break






