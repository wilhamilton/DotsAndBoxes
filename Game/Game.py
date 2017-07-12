"""The Game."""


class Game:
    """The game object."""

    def __init__(self, board, players):
        """Initialize a new game."""
        self.board = board
        self.players = players
        self.score = []

        for player in self.players:
            self.score.append(0)

    def play(self):
        """Play the game."""
        print(self.board)

        while self.board.number_squares < self.board.max_number_squares:
            for player in self.players:
                temp_move = player.request_move(self.board)
                print("Player: " + str(player.id))
                print("Move: " + str(temp_move))
                """Set edge (warn if illegal move attempted)"""
                if not self.board.set_edge(temp_move):
                    print("Illegal move requested by player, turn lost!")
                self.count_score()
                self.print_score()
                print(self.board)

        print("game over")
        self.print_score()

    def count_score(self):
        """Count the number of squares each player currently has."""
        for player in self.players:
            self.score[player.id] = 0
            for row in self.board.grid:
                for dot in row:
                    if dot.owner is player.id:
                        self.score[player.id] = self.score[player.id] + 1

    def print_score(self):
        """Print out the current score."""
        i = 0
        for score in self.score:
            print("player ", i, ": ", score)
            i = i + 1
