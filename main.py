"""Example Game."""

from Game.Board import Board
# from Game.Player import Player
from Game.Game import Game
from Players.RandomPlayer import RandomPlayer

board = Board([5, 5])

player1 = RandomPlayer(0)
player2 = RandomPlayer(1)

game = Game(board, [player1, player2])

game.play()

# temp = player2.request_move(board)

# print(temp)
# print(board)
# print("test")
