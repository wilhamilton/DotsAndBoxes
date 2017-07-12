"""
Test for CLIHumanPlayer class.  Doesn't actually assert anything yet
just plays, modify test later...
"""

import unittest

from Game.Board import Board
from Game.Game import Game
from Players.CLIHumanPlayer import CLIHumanPlayer

board = Board([3, 3])

player1 = CLIHumanPlayer(0)
player2 = CLIHumanPlayer(1)

game = Game(board, [player1, player2])

game.play()
