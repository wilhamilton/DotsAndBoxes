"""The Game."""


class Game:
    """The game object."""

    def __init__(self, board, players):
        """Initialize a new game."""
        self.board = board
        self.players = players

    def play(self):
        """Play the game."""
        print(self.board)

        while self.board.number_squares < self.board.max_number_squares:
            for player in self.players:
                temp_move = player.request_move(self.board)
                print("Player: " + str(player.id))
                print("Move: " + str(temp_move))
                self.board.set_edge(temp_move)
                print(self.board)

        print("game over")
