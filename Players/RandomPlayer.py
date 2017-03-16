"""Defines a random player class."""

from random import randint as randint

from Game.Player import Player
from Game.Move import Move


class RandomPlayer(Player):
    """A Player who makes random moves."""

    def request_move(self, board):
        """Request a random move based on the current game board."""
        i = randint(0, board.rows - 1)
        j = randint(0, board.cols - 1)

        if randint(0, 1) is 1:
            temp_direction = True
        else:
            temp_direction = False

        return Move([i, j], temp_direction, self.id)

    def check_move_against_board(self, move, board):
        """Check to see if a move is valid."""
        pass
