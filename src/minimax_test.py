# Test file for minimax.py

# Imports
from board import GameBoard
from minimax import Node, utility


def runTests():
    # testUtility2Row2Col()
    # testUtility3Row3Col()
    testUtility3Diag()


def testUtility2Row2Col():
    # Test for 2 x in row and 2 x in column with both sides open for each
    gameboard = GameBoard(5, 5)
    gameboard.placeMove(1, 1, "x")
    gameboard.placeMove(1, 2, "x")
    gameboard.placeMove(2, 1, "x")
    gameboard.printBoard()
    node = Node(gameboard, (2, 1), "x", 0)
    hn = utility(node)
    if hn != 40: 
        print("Expected 40 for heuristic but got", hn)


def testUtility3Row3Col():
    gameboard = GameBoard(5, 5)
    gameboard.placeMove(1, 1, "x")
    gameboard.placeMove(1, 2, "x")
    gameboard.placeMove(1, 3, "x")
    gameboard.placeMove(2, 1, "x")
    gameboard.placeMove(3, 1, "x")
    gameboard.printBoard()
    node = Node(gameboard, (3, 1), "x", 0)
    hn = utility(node)
    print(hn)
    if hn != 400: 
        print("Expected 400 for heuristic but got", hn)

def testUtility3Diag():
    gameboard = GameBoard(5, 5)
    gameboard.placeMove(1, 1, "x")
    gameboard.placeMove(2, 2, "x")
    gameboard.placeMove(3, 3, "x")
    gameboard.printBoard()
    node = Node(gameboard, (3, 3), "x", 0)
    hn = utility(node)
    print(hn)
    if hn != 200: 
        print("Expected 200 for heuristic but got", hn)







runTests()