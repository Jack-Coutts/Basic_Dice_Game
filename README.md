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
3. Run the following command to start the game: `python dice_game.py` or `python3 dice_game.py`
4. Follow the on-screen instructions to play the game.

## Scoring System Explanation

The scoring system in the dice game is designed to reward players for rolling multiple dice with the same value. The scores are squared, cubed, or raised to the fourth power based on the number of matching dice:

1. Rolling three of the same number: (number * 3)^2 points
2. Rolling four of the same number: (number * 4)^3 points
3. Rolling five of the same number: (number * 5)^4 points

The exponential scoring system has several benefits:

- It creates a significant difference in scores between rolling three, four, or five of the same number, making the game more exciting and rewarding for lucky rolls.
- It reflects the rarity and difficulty of rolling multiple dice with the same value, assigning much higher scores to more difficult combinations.
- It provides a catch-up mechanism, allowing trailing players to quickly close the gap or take the lead with a high-scoring combination.
- It creates exciting moments in the game when a player rolls a high-scoring combination.

Rolling a straight (1, 2, 3, 4, 5) is considered a special and rare occurrence, so a fixed score of 1,500 points is assigned to it. This adds variety to the game and provides another way for players to achieve a high score.

The specific choice of exponents (squaring for three of a kind, cubing for four of a kind, and raising to the fourth power for five of a kind) is somewhat arbitrary. The main idea is to have an exponential increase in scores as the number of matching dice increases. The scoring system can be adjusted based on preferred level of scoring and game balance.

## Game Rules

- The game is played between the player and the computer.
- Each round, both the player and the computer roll five dice.
- The player has the chance to re-roll the dice up to three times per round to try and get a higher score.
- The game lasts for ten rounds.
- The scoring rules are as follows:
- If you roll three of the same number, you get (number * 3)^2 points.
- If you roll four of the same number, you get (number * 4)^3 points.
- If you roll five of the same number, you get (number * 5)^4 points.
- If you roll a straight (1, 2, 3, 4, 5 or 2, 3, 4, 5, 6), you get 1500 points.
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


## Unit Tests

Unit tests are an additional part of this project, ensuring the correctness and reliability of the dice game code. They are automated tests that verify the behavior of individual units or components of the code in isolation.

### What are Unit Tests?

Unit tests are small, focused tests that validate the functionality of specific parts of the code, such as functions or methods. They are written to test a single unit of code in isolation, independent of other parts of the system. Unit tests help catch bugs, prevent regressions, and provide confidence in the code's correctness.

In this project, unit tests are written using the `unittest` framework, a built-in testing framework in Python. Each test case is defined as a separate method within a test class, and assertions are used to verify the expected behavior of the code.

### Why Use Unit Tests?

Unit tests offer several benefits:

1. **Correctness**: Unit tests help ensure that the code behaves as expected and produces the correct output for various inputs and scenarios.

2. **Bug Detection**: By running unit tests regularly, you can catch bugs early in the development process, making it easier to identify and fix issues.

3. **Regression Prevention**: Unit tests serve as a safety net, preventing regressions and ensuring that existing functionality remains intact as the codebase evolves.

4. **Code Quality**: Writing unit tests encourages better code design, promotes modularity, and helps maintain a clean and maintainable codebase.

5. **Documentation**: Unit tests act as a form of documentation, describing the expected behavior of the code and serving as examples of how to use the various components.

### Running the Unit Tests

To run the unit tests for the dice game, follow these steps:

1. Make sure you have Python installed on your system.

2. Open a terminal or command prompt and navigate to the project's root directory.

3. Run the following command to execute the unit tests: `python -m unittest discover tests -v`. This command tells Python to discover and run all the unit tests found in the `tests/` directory as long as test file naming conventions for unittest are followed.

4. The test results will be displayed in the console, indicating which tests passed or failed. If any tests fail, the console output will provide details about the failures, including the specific test cases and any error messages.

5. If all tests pass, you will see a summary indicating the total number of tests run and the success status.

By running the unit tests regularly, you can ensure that the dice game code remains reliable and functions as expected. It is good practice to run the tests whenever making changes to the codebase and before deploying the game to catch any potential issues early on.

Remember to keep the unit tests up to date as you modify or add new features to the game. Whenever you introduce new functionality or make changes to existing code, consider writing corresponding unit tests to maintain the code's quality and reliability.