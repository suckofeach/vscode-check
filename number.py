from curses.ascii import isdigit
import random

top_range = input('type a numb ')

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print('please print greater than 0')

else:
    print('type number pls')

r = random.randint(1, top_range)

count = 0

while True:
    count += 1
    guess = input('make a guess ')

    if guess.isdigit():
        guess = int(guess)
    else:
        print('type num pls next time')
        continue

    if guess == r:
        print('u got it')
        break
    elif guess > r:
        print('above')
    else:
        print('below')

print('u got in in', count, 'guesses')