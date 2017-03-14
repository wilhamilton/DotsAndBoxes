"""
Unit tests for the Board object.

For example, test that it can display itself (to-string version only for now).
Note, root project dir (at level of git repo) must be in PYTHONPATH to run this from tests folder.
"""

import unittest
from Game.Board import Board
from Game.Move import Move

class TestBoard(unittest.TestCase):

    def setUp(self):
        pass

    def test_DisplayAsString(self):
        """ Try making some moves, simple 2x2, see that displays properly """

        pID1 = 1 
        pID2 = 2 # Noting horizontal is true for edge dir...
        moves = [
                Move([0,0],True,pID1),
                Move([0,0],False,pID2),
                Move([1,0],True,pID1),
                Move([0,1],False,pID2)
        ]
        # Fourth move there should complete owned square for player pID2
        moves += [
                Move([1,1],False,pID1),
                Move([2,1],True,pID2),
                Move([1,2],False,pID1),
                Move([1,0],False,pID2)
        ]

        # Note - dims passed in here are the number of dots, not boxes
        btest1 = Board([3,3])
        for m in moves:
            btest1.setEdge(m)

        # Try displaying and see if matches expected result
        expectS = ( "*---*   *\n"
                    "| B |    \n"
                    "*---*   *\n"
                    "|   |   |\n"
                    "*   *---*\n")
        debugmsg = "\n\n" + str(btest1) + "\n\n" + expectS + "\n\n"
        self.assertEqual(str(btest1), expectS, debugmsg)
    

# Run the tests if this is your top-level
if __name__ == '__main__':
    unittest.main()
