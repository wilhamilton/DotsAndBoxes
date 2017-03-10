"""Example Game."""

from Game.Board import Board
from Game.Player import Player
from Game.Game import Game

board = Board([5, 5])

player1 = Player(1)
player2 = Player(2)

game = Game(board, [player1, player2])

game.play()

print("test")
