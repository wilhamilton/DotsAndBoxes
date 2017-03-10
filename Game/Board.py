"""
The Game Module.

The game module is used to represent the game board for Dots and Boxes.
"""

from Game.Dot import Dot


class Board:
    """The actual game class."""

    def __init__(self, gridSize):
        """Initialize the game object."""
        self.grid = []

        for i in range(0, gridSize[0]):
            new = []
            for j in range(0, gridSize[1]):
                new.append(Dot())
            self.grid.append(new)

    def setEdge(self, move):
        """Update the gameboard based on a move."""
        pass

    def draw(self):
        """Output the Gameboard visually."""
