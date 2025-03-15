import random

value = random.randint(0, 10)

name = input("Hello please enter your name: ")
print(f"Hello {name}")
guess = 0

while guess != value:
    guess = int(input("Guess a number from 0-10: "))
    
    if guess > value:
        print("Guess lower")
    elif guess < value:
        print("Guess higher")
    else:
        print("You guessed correctly")