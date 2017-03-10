"""Example Game."""

import Game.Board as Board
import Game.Player as Player

gameBoard = Board([5, 5])

player1 = Player(1)
player2 = Player(2)

game = Game(board, [player1, player2])

game.play()
