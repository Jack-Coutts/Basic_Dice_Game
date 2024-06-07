# Dice Game

This project implements a dice game where the player competes against the computer. The game involves rolling five dice and trying to achieve the highest possible score. The player and the computer take turns rolling the dice and have the opportunity to re-roll up to three times per round to improve their score. The game lasts for ten rounds, and the player with the highest total score at the end wins.

## Task Description

The task is to create a dice game with the following requirements:

- The game involves a player competing against the computer.
- Both the player and the computer roll five dice each round.
- The player has the chance to re-roll the dice up to three times per round to try and get a higher score.
- The game lasts for ten rounds.
- The player with the highest total score at the end of the ten rounds wins.
- The computer's decision to re-roll is based on a strategy (can be simple or complex).
- The player interacts with the program to decide whether to re-roll or not.
- At the end of the game, the player is offered the chance to play again.

## Getting Started

To run the dice game, make sure you have Python installed on your system. Then, follow these steps:

1. Clone the repository or download the `dice_game.py` file.
2. Open a terminal or command prompt and navigate to the directory where the file is located.
3. Run the following command to start the game: ```python dice_game.py``` or ```python3 dice_game.py```
4. Follow the on-screen instructions to play the game.

## Game Rules

- The game is played between the player and the computer.
- Each round, both the player and the computer roll five dice.
- The player has the chance to re-roll the dice up to three times per round to try and get a higher score.
- The game lasts for ten rounds.
- The scoring rules are as follows:
- If you roll three of the same number, you get (number * 3)^2 points.
- If you roll four of the same number, you get (number * 4)^3 points.
- If you roll five of the same number, you get (number * 5)^4 points.
- If you roll a straight (1, 2, 3, 4, 5), you get 1500 points.
- The player with the highest total score at the end of the ten rounds wins.

## Code Structure

The code is organized into the following sections:

- `display_game_description()`: Displays a description of the dice game to the user.
- `Dice` class: Represents the dice used in the game and provides a method to roll the dice.
- `Player` class: Represents a player (either the user or the computer) and provides methods to play a round and get user decisions.
- `calculate_score(rolls)`: Calculates the score for a given set of dice rolls based on the scoring rules.
- `computer_strategy(dice, score, rerolls_left)`: Implements the computer's strategy to decide whether to re-roll the dice.
- `play_round(player, computer, dice, round_num)`: Plays a single round of the game.
- `play_game()`: Plays the complete dice game, including multiple rounds and determining the winner.

The `if __name__ == "__main__":` block at the end of the code serves as the entry point of the program. It displays the game description and starts the game when the file is executed directly.

