# import random module from library
import random


print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#randint == generate random number from specied rnage
num = random.randint(1, 10)
isGuessRight = False

#while loop

while isGuessRight != True:
    guess = input("guess number between 1 and  10: ")
    print(type(guess))
    if int(guess) == num:
        print("you guess {}. That's correct!".format(guess))
        isGuessRight = True
    else:
        print("you guess {}. Sorry, try again".format(guess))
        