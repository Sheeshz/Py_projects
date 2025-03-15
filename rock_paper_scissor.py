import random

while True:

    choices = ['rock','paper','scissor']
    output = random.choice(choices)

    user_input = input("Enter choice(rock,paper,scissor): ")

    if output == user_input:
        print("Draw")
    elif user_input == 'rock':
        if output == 'scissor':
            print("You win")
        else:
            print("You lose")
    elif user_input == 'paper':
        if output == 'rock':
            print("You win")
        else:
            print("You lose")
    elif user_input == 'scissor':
        if output == 'paper':
            print("You win")
        else:
            print("You lose")
            
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break