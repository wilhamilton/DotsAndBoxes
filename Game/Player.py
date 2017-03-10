"""
The Player Class.

Defines a player in the game.
"""

from Game import Board
from Game import Move


class Player:
    """The base player object."""

    def __init__(self, id):
        """Create a player."""
        self.id = id

    def makeMove(self, board):
        """Make a game move based on the current gameboard state."""
        myMove = Move([0, 0], True, self.id)
        return myMove
