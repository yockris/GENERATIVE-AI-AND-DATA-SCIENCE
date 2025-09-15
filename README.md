# Rock, Paper, Scissors Game

This is a simple command-line implementation of the classic Rock, Paper, Scissors game in Python.  
The user plays against the computer, which randomly selects its move.

## Features

- Accepts user input for "rock", "paper", or "scissors"
- Validates user input and prompts again if invalid
- Randomly selects the computer's choice
- Determines and displays the winner

## How to Run

1. Make sure you have Python installed on your system.
2. Clone or download this repository.
3. Open a terminal and navigate to the project directory.
4. Run the game using:

   ```
   python GAIDS_Task-1.py
   ```

## Code Structure

- **choices**: List of valid options.
- **get_user_choice()**: Prompts and validates user input.
- **get_computer_choice()**: Randomly selects the computer's move.
- **select_winner()**: Determines the winner based on the rules.
- **play_game()**: Main function that runs the game.

## Example Gameplay

```
Enter rock, paper, or scissors: rock
You chose: rock
Computer chose: scissors
You win!
```

## License

This project is open source and free to use.
