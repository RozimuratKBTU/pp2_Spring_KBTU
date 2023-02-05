import random

print('Hello! What is your name? ')
name = input()
print(" Well,",name,",I am thinking of a number between 1 and 20.")

guess = random.randint(1,20)
print('Take a guess.')
Number = int(input())
counter = 1

while Number != guess:
    if Number < guess:
        print('Your guess is too low.')
    elif Number > guess:
        print('Your guess is too high.')
    print("Take a guess.")
    Number = int(input())
    counter = counter + 1


print('Good job,',name ,',You guessed my number in',counter,'guesses!')