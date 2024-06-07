import random

# Constants
NUM_DICE = 5
NUM_ROUNDS = 10
MAX_REROLLS = 3
STRAIGHT_SCORE = 1500


def display_game_description():
    """Display a description of the dice game to the user."""
    print("Welcome to the Dice Game!")
    print("In this game, you will be playing against the computer.")
    print(f"Each round, you and the computer will roll {NUM_DICE} dice.")
    print(f"You will have the chance to re-roll the dice up to {MAX_REROLLS} times to try and get a higher score.")
    print(f"The game will last for {NUM_ROUNDS} rounds, and the player with the highest total score at the end wins.")
    print("Scoring rules:")
    print("- If you roll three of the same number, you get (number * 3)^2 points.")
    print("- If you roll four of the same number, you get (number * 4)^3 points.")
    print("- If you roll five of the same number, you get (number * 5)^4 points.")
    print(f"- If you roll a straight (1, 2, 3, 4, 5), you get {STRAIGHT_SCORE} points.")
    print("Good luck and have fun!\n")


class Dice:
    def __init__(self, num_dice=NUM_DICE):
        self.num_dice = num_dice

    def roll(self):
        """Roll the dice and return the values."""
        return [random.randint(1, 6) for _ in range(self.num_dice)]


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def play_round(self, dice):
        """Play a single round of the dice game."""
        print(f"\n{self.name}'s turn:")
        rolls = dice.roll()
        print(f"Initial roll: {rolls}")

        score = calculate_score(rolls)
        print(f"Score: {score}")

        for i in range(MAX_REROLLS):
            keep_rolling = self.get_user_decision(f"Roll again? (y/n) ({i + 1}/{MAX_REROLLS}) ")
            if not keep_rolling:
                break
            rolls = dice.roll()
            print(f"New roll: {rolls}")
            score = calculate_score(rolls)
            print(f"Score: {score}")

        self.score += score
        return score

    def get_user_decision(self, prompt):
        """Get user decision with input validation."""
        while True:
            decision = input(prompt).strip().lower()
            if decision == 'y':
                return True
            elif decision == 'n':
                return False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


def calculate_score(rolls):
    """Calculate the score for a set of dice rolls."""
    counts = [rolls.count(i) for i in range(1, 7)]
    score = 0

    # Score for multiples
    score_map = {
        3: lambda x: (x * 3) ** 2,
        4: lambda x: (x * 4) ** 3,
        5: lambda x: (x * 5) ** 4
    }
    for i, count in enumerate(counts, start=1):
        if count in score_map:
            score += score_map[count](i)

    # Score for straights
    if set(rolls) == {1, 2, 3, 4, 5} or set(rolls) == {2, 3, 4, 5, 6}:
        score += STRAIGHT_SCORE

    return score


def computer_strategy(score, rerolls_left):
    """Computer strategy to decide whether to roll again."""
    if score < 300 and rerolls_left > 0:
        return True
    return False


def play_round(player, computer, dice, round_num):
    """Play a single round of the game."""
    print(f"\nRound {round_num}")
    player_round_score = player.play_round(dice)
    print(f"Player score for round {round_num}: {player_round_score}")
    print(f"Player total score: {player.score}")

    computer_round_score = 0
    computer_rerolls_left = MAX_REROLLS
    while computer_strategy(computer_round_score, computer_rerolls_left):
        computer_round_score = calculate_score(dice.roll())
        computer_rerolls_left -= 1
    computer.score += computer_round_score
    print(f"Computer score for round {round_num}: {computer_round_score}")
    print(f"Computer total score: {computer.score}")


def play_game():
    """Play the complete dice game."""
    player = Player("Player")
    computer = Player("Computer")
    dice = Dice(NUM_DICE)

    for round_num in range(1, NUM_ROUNDS + 1):
        play_round(player, computer, dice, round_num)

    print("\nGame over!")
    if player.score > computer.score:
        print("Congratulations, you won!")
    elif player.score < computer.score:
        print("Sorry, the computer won.")
    else:
        print("It's a tie!")

    play_again = input("Play again? (y/n) ").strip().lower() == "y"
    if play_again:
        play_game()


if __name__ == "__main__":
    display_game_description()
    play_game()

