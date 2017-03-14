"""
A Dot on the gameboard.

This class represents a dot. Dots are also responsible for creating edges and
squares in the game.  As such a dot has 3 properties:
    - a vertical edge
    - a horizontal edge
    - an owner (defining is as a square)

Every dot is the upper-left corner of the square it defines.  It is also the
left end point of the horizontal edge it defines and the upper end point
of the vertical edge it defines.

The structure of a single dot is as follows:

    O--
    |S

Where O represents the dot, -- a horizontal edge, | a vertical edge, and S
represents a square.

The logic for determining whether a dot should define a square is
contained in the game board class.  A dot simply stores whether or not it
is a square.
"""


class Dot:
    """This is the class for a single dot in the game."""

    def __init__(self):
        """
        Initialize a dot.

        A dot starts with no edges and no owner (associated square).
        A dot does not need to know its own position.  This data is maintained
        by the game board class.
        """
        self.vertical = None      # we do not start with a vertical edge
        self.horizontal = None    # we do not start with a horizontal edge
        self.owner = None         # we do not have an owner (not a square)

    def set_vertical_edge(self, player_id):
        """
        Set the status for this dot as having a vertical edge.

        A vertical edge extends down from this dot.
        We return true if we are able to set this edge.  We return False
        if the edge was already defined.
        """
        if self.vertical is None:
            # this dot does not have a vertical edge, create one
            self.vertical = player_id
            return True
        else:
            return False

    def set_horizontal_edge(self, player_id):
        """
        Set the status for this dot as having a horizontal edge.

        A horizontal edge extends to the right from this dot.
        We return true if we are able to set this edge.  We return False
        if the edge was already defined.
        """
        if self.horizontal is None:
            # this dot does not have a horizontal edge, create one
            self.horizontal = player_id
            return True
        else:
            return False

    def set_as_square(self, player_id):
        """
        Set the owner of the square this dot defines.

        A square is defined by the dot in its upper-left corner.
        We return true if we properly set the owner and false if this
        dot/square is already owned.
        """
        if self.owner is None:
            # this dot does not yet define a squre, update it so it does
            self.owner = player_id
            return True
        else:
            return False
