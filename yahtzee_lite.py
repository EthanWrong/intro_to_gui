"""Non-functioning overcomplicated program"""

import random
from easygui import *


class Player:
    def __init__(self, iteration):
        self.iteration = iteration  # allows to ask player {i}
        self.name = "player"
        self.score = 0

    def get_name(self):
        self.name = enterbox(f"Enter name of player {self.iteration}").capitalize()

    def add_points(self, points, reason):
        self.score += points
        msgbox(f"{reason}!\n\n{self.name} gets {points} points.\n\n"
               f"{self.name}'s score: "
               f"{self.score}")


# generates a list of 5 randomly rolled dice
def roll_dice():
    dice = []
    for i in range(5):
        dice.append(random.randint(1, 6))
    return dice


def calc_score(dice):
    for num in range(1, 6):
        if dice.count(num) == 3:
            return 10, "Three of a kind"
        elif dice.count(num) == 4:
            return 30, "Four of a kind"
        elif dice.count(num) == 5:
            return 50, "YAHTZEE"


def get_player(i):
    player = Player(i)
    player.get_name()
    return player


def get_players():
    players = []
    i = 1
    while len(players) < 1 or ynbox("Would you like to add another player?"):
        players.append(get_player(i))
        i += 1

    return players


def play_turn(player):
    roll = 1
    msgbox(f"{player.name}'s turn!\n\nClick 'OK' to roll")
    while roll <= 3:
        player_dice = roll_dice()
        choice = buttonbox(f"{player.name}: dice roll {roll}\nCurrent "
                           f"score: {player.score}\n\nYou rolled: "
                           f"{player_dice}",
                           choices=["Roll Again", "Stick"])
        if choice == "Roll Again":
            roll += 1
        elif choice == "Stick":
            points, reason = calc_score(player_dice)
            player.add_points(points, reason)
            return player
    msgbox(f"{player.name}: You don't have any rolls left.")


def play_round(players):
    for player in players:
        player = play_turn(player)

    top_score = 0
    winners = []
    for player in players:
        if player.score > top_score:
            top_score = player.score
            winners = [player]
        elif player.score == top_score:
            winners.append(player)

    if len(winners) == 1:
        msgbox(f"{winners[0].name} wins with a score of {winners[0].score}!")
    else:
        msgbox(f"This was a draw!")


my_players = get_players()
play_round(my_players)









