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
        self.rows = gridSize[0]
        self.cols = gridSize[1]

        # create the gameboard as a 2D array of dots
        for i in range(0, self.rows):
            newRow = []
            for j in range(0, self.cols):
                newRow.append(Dot())
            self.grid.append(newRow)

    def setEdge(self, move):
        """Update the gameboard based on a move."""
        i = move.coordinate[0]
        j = move.coordinate[1]

        if move.edgeDirection:
            # horizontal edge indicated by edgeDirection == true
            returnVal = self.grid[i][j].setHorizontalEdge(move.player)
        else:
            returnVal = self.grid[i][j].setVerticalEdge(move.player)

        if returnVal:
            self.checkSquares(i, j, move.edgeDirection)

        return returnVal

    def checkSquares(self, i, j, edge):
        """Check to see if the edge just added produced a square."""
        if i < self.rows and j < self.cols:
            # we only want to check this square if it's not on the bottom/right
            self.isSquare(i, j)

        if edge:
            # we created a horizontal edge, we need to check the square above
            if i-1 >= 0:
                # make sure we are not at the top of the board
                self.isSquare(i-1, j)
        else:
            if j-1 >= 0:
                # make sure we are not at the left side of the board
                self.isSquare(i, j-1)
        pass

    def isSquare(self, i, j):
        """Check to see if the current dot (defined by i,j) is a square."""
        dot = self.grid[i][j]
        right = self.grid[i][j+1]
        bottom = self.grid[i+1][j]

        if dot.horizontal is not None and dot.vertical is not None:
            # do a thing
            pass
        pass

    def draw(self):
        """Output the Gameboard visually."""
        pass
