"""
The Game Module.

The game module is used to represent the game board for Dots and Boxes.
"""

from Game.Dot import Dot


class Board:
    """The actual game class."""

    def __init__(self, grid_size):
        """Initialize the game object."""
        self.grid = []
        self.rows = grid_size[0]
        self.cols = grid_size[1]
        self.number_squares = 0
        self.max_number_squares = (self.rows - 1) * (self.cols-1)

        # create the gameboard as a 2D array of dots
        for i in range(0, self.rows):
            new_row = []
            for j in range(0, self.cols):
                new_row.append(Dot())
            self.grid.append(new_row)

    def set_edge(self, move):
        """Update the gameboard based on a move."""
        # get the location of the dot we will be trying to set an edge for
        i = move.coordinate[0]  # get the row the dot is in
        j = move.coordinate[1]  # get the column the dot is in

        if move.edge_direction:
            # horizontal edge indicated by edge_direction being true
            return_val = self.grid[i][j].set_horizontal_edge(move.player)
        else:
            # vertical edge
            return_val = self.grid[i][j].set_vertical_edge(move.player)

        if return_val:
            # we were able to set an edge so we need to check to see if we
            # created any new squares when that edge was added
            self.check_for_squares(move)

        return return_val

    def check_for_squares(self, move):
        """Check to see if the edge just added produced a square."""
        # get the location of the dot we will be trying to set an edge for
        i = move.coordinate[0]  # get the row the dot is in
        j = move.coordinate[1]  # get the column the dot is in

        if i < self.rows-1 and j < self.cols-1:
            # we only want to check this square if it's not on the bottom/right
            self.is_a_square(i, j, move.player)

        # whenever we create an edge we have the possibility of creating more
        # than one square.  check for those other squares
        if move.edge_direction:
            # we created a horizontal edge, we need to check the square above
            if i-1 >= 0:
                # make sure we are not at the top of the board
                self.is_a_square(i-1, j, move.player)
        else:
            if j-1 >= 0:
                # make sure we are not at the left side of the board
                self.is_a_square(i, j-1, move.player)
        pass

    def is_a_square(self, i, j, player):
        """Check to see if the current dot (defined by i,j) is a square."""
        # print("i, j, row, cols", i, " ", j, " ", self.rows, " ", self.cols)
        if i+1 >= self.rows or j+1 >= self.cols:
            # print("out of bounds")
            return False

        dot = self.grid[i][j]
        right = self.grid[i][j+1]
        bottom = self.grid[i+1][j]

        if dot.horizontal is not None and dot.vertical is not None:
            # the current dot has both edges, see if the neighbors have the
            # appropriate edges
            if right.vertical is not None and bottom.horizontal is not None:
                # out neighbors have the correct edges, we have a square
                self.number_squares = self.number_squares + 1
                return self.grid[i][j].set_as_square(player)

        # we only get here if we don't have a square
        return False

    def draw(self):
        """Output the Gameboard visually."""
        # Intending to use matplotlib here?
        pass

    def __str__(self):
        """
        To string function.

        Prints game board as a serires of dashes/pipes
         e.g. for shell print
        """
        outstr = ""
        for i, row in enumerate(self.grid):
            # Build the string for one row here, starting with *'s for dots
            for j, dot in enumerate(row):
                outstr += "o"
                # For all but right-most dot in row,
                # draw horizontal lines as necessary
                if j != len(row)-1:
                    outstr += "---" if dot.horizontal is not None else "   "
            # Then add in the vertical lines below the dots,
            # and indicate owner if any
            # Note this doesn't apply for the last row
            if i != len(self.grid)-1:
                outstr += '\n'
                for j, dot in enumerate(row):
                    outstr += "|" if dot.vertical is not None else " "
                    # If not in the last column, write " <owner> " or "   "
                    if j != len(row)-1:
                        outstr += "   " if dot.owner is None else " " \
                            + str(dot.owner) + " "
                outstr += '\n'

        return outstr
