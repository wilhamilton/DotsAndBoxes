"""
A Move in the game.

The move in the game is a player drawing an edge from a dot.  This class
is just a container to store all of the properties that define a move in
the game.  The properties that define a move are:

coordinate      -   the location [i, j] on the game board of the dot
                    that is the base point for an edge

edge_direction  -   whether the edge is horizontal (true) or
                    vertical (false)

player_id       -   the id of the player who is making the move

The class does not have any methods.
"""


class Move:
    """A Move in the Game."""

    def __init__(self, coordinate, edge_direction, player_id):
        """
        Create a game move.

        The input parameters correspond to the properties of the class.
        """
        self.coordinate = coordinate            # location of base dot
        self.edge_direction = edge_direction    # direction of new edge
        self.player = player_id                 # player making the move

    def __str__(self):
        """Print out a move for debugging."""
        return "[" + str(self.coordinate[0]) + ", " + str(self.coordinate[1]) \
            + "]" + "dir: " + str(self.edge_direction)
