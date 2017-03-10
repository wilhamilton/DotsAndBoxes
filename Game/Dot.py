"""
Dot.

This class represents a dot.  A dot has 3 properties: a vertical edge, a
horizontal edge, and an owner.

Every dot is the upper-left corner of a square (and the corresponding) edges.
"""


class Dot:
    """This is the class for a single dot in the game."""

    def __init__(self):
        """Initialize a dot."""
        self.vertical = None      # we do not start with a vertical edge
        self.horizontal = None    # we do not start with a horizontal edge
        self.owner = None         # we do not have an owner (not a square)

    def setVerticalEdge(self, playerId):
        """
        Set the status for this dot as having a vertical edge.

        A vertical edge extends down from this dot.
        """
        self.vertical = playerId

    def setHorizontalEdge(self, playerId):
        """
        Set the status for this dot as having a horizontal edge.

        A horizontal edge extends to the right from this dot.
        """
        self.horizontal = playerId
