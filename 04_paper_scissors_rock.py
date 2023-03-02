import easygui, random

weapons = ["paper", "scissors", "rock"]
scores = {"player": 0, "computer": 0, "draw": 0, "total": 0}


def play_round():
    easygui.msgbox("Welcome to Paper-Scissors-Rock. \n"
                   "Paper beats Rock,\n"
                   "Rock beats Scissors,\n"
                   "Scissors beats Paper.\n"
                   "\n"
                   "Ready?", "Welcome and Rules")

    player = easygui.buttonbox("Choose your weapon", "Choose weapon",
                               choices=weapons)

    computer = random.choice(weapons)

    if player == computer:
        winner = "draw"
    elif player == "paper":
        winner = "player" if computer == "rock" else "computer"
    elif player == "scissors":
        winner = "player" if computer == "paper" else "computer"
    elif player == "rock":
        winner = "player" if computer == "scissors" else "computer"

    scores[winner] += 1
    scores["total"] += 1

    msg1 = f"You chose {player.capitalize()} and the computer chose " \
           f"{computer.capitalize()}"

    if winner == "draw":
        msg2 = "--This was a draw--"
    elif winner == "player":
        msg2 = "**You won**"
    elif winner == "computer":
        msg2 = "..You lost.."

    msg3 = f"Player: {scores['player']}, \n" \
           f"Computer: {scores['computer']}, \n" \
           f"Rounds: {scores['total']}"

    repeat = False
    repeat = easygui.ynbox(f"{msg1}\n\n{msg2}\n{msg3}\n\nAgain?", "Outcome")
    if repeat:
        play_round()


play_round()
