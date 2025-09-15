#Building the Rock, Paper, Scissors Game

#import random module
import random

#list of possible options

choices = ['rock', 'paper', 'scissors']

#function to get user choice
def get_user_choice():
    user_choice = input('Enter rock, paper, or scissors: ').lower()
    while user_choice not in choices:
        user_choice = input('Invalid choice. Please enter rock, paper, or scissors: ').lower()
    return user_choice
    
#function to get computer choice
def get_computer_choice():
    computer_choice = random.choice(choices)
    return computer_choice

#function to determine the winner
def select_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'It is a tie!' 
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'You win!'
    else:
        return 'computer wins!'
    
#main function to play the game
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f'You chose: {user_choice}')
    print(f'Computer chose: {computer_choice}')
    result = select_winner(user_choice, computer_choice)
    print(result)
    
play_game()