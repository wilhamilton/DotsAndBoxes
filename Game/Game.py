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

        # Loop until all squares taken...
        player_index = 0
        nsquares_last = 0
        while self.board.number_squares < self.board.max_number_squares:
            print(self.board)
            player = self.players[player_index]
            print("Player: " + str(player.id))
            temp_move = player.request_move(self.board)
            print("Move: " + str(temp_move))
            """Set edge (warn if illegal move attempted)"""
            if not self.board.set_edge(temp_move):
                print("Illegal move requested by player, turn lost!")
            self.count_score()
            self.print_score()
            
            # If player did not make a box, go to next player
            if self.board.number_squares == nsquares_last:
                player_index = (1 + player_index) % len(self.players)
            else:
                nsquares_last = self.board.number_squares

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
        print("Score so far:")
        for score in self.score:
            print("player ", i, ": ", score)
            i = i + 1
