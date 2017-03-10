"""The Game."""


class Game:
    """The game object."""

    def __init__(self, board, players):
        """Initialize a new game."""
        self.board = board
        self.players = players

    def play(self):
        """Play the game."""
