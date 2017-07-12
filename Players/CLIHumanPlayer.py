"""Defines a human player class that takes move choice from cmd line."""

from sys import stdin

from Game.Player import Player
from Game.Move import Move


class CLIHumanPlayer(Player):
    """A Player where move is read from stdin command line."""

    def request_move(self, board):
        """Game already displays board, ask user for coords to play"""
        print("Enter move as: 'i,j,dir', with dir = H or V, then hit enter.")
        print("  Example input: 1,2,V")

        inpts = stdin.readline().split(',')

        i = int(inpts[0])
        j = int(inpts[1])
        temp_direction = (inpts[2].strip() == 'H') 

        return Move([i, j], temp_direction, self.id)

    def check_move_against_board(self, move, board):
        """Check to see if a move is valid."""
        pass
