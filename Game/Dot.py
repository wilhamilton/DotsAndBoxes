"""
A Dot on the gameboard.

This class represents a dot.  A dot has 3 properties: a vertical edge, a
horizontal edge, and an owner.

Every dot is the upper-left corner of a square (and the corresponding) edges.
"""


class Dot:
    """This is the class for a single dot in the game."""

    def __init__(self):
        """
        Initialize a dot.

        A dot starts with no edges and no owner (associated square).
        """
        self.vertical = None      # we do not start with a vertical edge
        self.horizontal = None    # we do not start with a horizontal edge
        self.owner = None         # we do not have an owner (not a square)

    def setVerticalEdge(self, playerId):
        """
        Set the status for this dot as having a vertical edge.

        A vertical edge extends down from this dot.
        We return true if we are able to set this edge.  We return False
        if the edge was already defined.
        """
        if self.vertical is None:
            self.vertical = playerId
            return True
        else:
            return False

    def setHorizontalEdge(self, playerId):
        """
        Set the status for this dot as having a horizontal edge.

        A horizontal edge extends to the right from this dot.
        We return true if we are able to set this edge.  We return False
        if the edge was already defined.
        """
        if self.horizontal is None:
            self.horizontal = playerId
            return True
        else:
            return False

    def setOwner(self, playerId):
        """
        Set the owner of the square this dot defines.

        A square is defined by the dot in its upper-left corner.
        We return true if we properly set the owner and false if this
        dot/square is already owned.
        """
        if self.owner is None:
            self.owner = playerId
            return True
        else:
            return False
