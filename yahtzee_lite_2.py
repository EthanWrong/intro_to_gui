from easygui import *
import random


def roll_dice():
    dice = []
    for num in range(5):
        dice.append(random.randint(1, 6))
    return dice


def stick(dice):
    for num in range(1, 7):
        if dice.count(num) == 3:
            return 10, "Three of a Kind"
        elif dice.count(num) == 4:
            return 30, "Four of a Kind"
        elif dice.count(num) == 5:
            return 50, "YAHTZEE!"
    return 0, "Better luck next time"


def play_turn(player):
    i = 1
    msgbox(f"{player['name']}, ready to roll?")
    while i <= 3:
        dice = roll_dice()
        choice = buttonbox(
            f"{player['name']}'s dice roll {i}\n\n"
            f"{player['name']} rolled: {dice}",
            "Random roll",
            choices=["Roll Again", "Stick"]
        )
        if choice == "Roll Again":
            i += 1
        elif choice == "Stick":
            points, msg = stick(dice)
            msgbox(
                f"{dice}\n\n"
                f"{msg}\n\n"
                f"{player['name']}'s points: {points}",
                "Result"
            )
            return points
    msgbox(
        f"{player['name']} ran out of rolls!\n\n"
        f"You score 0. Better luck next time",
        "Result"
    )
    return 0


def play_round(p1, p2):
    # players play their turns
    p1["points"] = play_turn(p1)
    p2["points"] = play_turn(p2)

    # figure out winner
    if p1["points"] > p2["points"]:
        winner, loser = p1, p2
    elif p1["points"] == p2["points"]:
        winner = "draw"
    else:
        winner, loser = p2, p1

    # display accordingly
    if winner == "draw":
        if ynbox(f"This was a draw!\n"
                 f"Both {p1['name']} and {p2['name']} scored "
                 f"{p1['points']}\n\n"
                 f"Do you want to play another round?",
                 "Round result"):
            return play_round(p1, p2)
    else:
        if ynbox(f"The winner is {winner['name']} with a score of "
                 f"{winner['points']}!\n\n"
                 f"{loser['name']} only scored {loser['points']}\n\n"
                 f"Would you like to play another round?",
                 "Round result"):
            return play_round(p1, p2)
    return msgbox("Goodbye", "See ya!")




# get player names
p1, p2 = {}, {}
p1["name"] = enterbox("Enter the name of player 1:", "Player 1").capitalize()
p2["name"] = enterbox("Enter the name of player 2:", "Player 2").capitalize()


play_round(p1, p2)
