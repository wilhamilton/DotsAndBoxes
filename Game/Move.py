"""
A Move in the game.

A move includes the base dot, the direction of an edge, and the player who
made the move.
"""


class Move:
    """A Move in the Game."""

    def __init__(self, coordinate, edgeDirection, playerId):
        """Create a game move."""
        self.coordinate = coordinate
        self.edgeDirection = edgeDirection
        self.player = playerId
