"""
The Game Module.

The game module is used to represent the game board for Dots and Boxes.
"""

from Game import Dot


class Board:
    """The actual game class."""

    def __init__(self, gridSize):
        """Initialize the game object."""
        for i in gridSize[0]:
            for j in gridSize[1]:
                self.grid[i][j] = Dot()

    def setEdge(self, move):
        """Update the gameboard based on a move."""
        pass

    def draw(self):
        """Output the Gameboard visually."""
