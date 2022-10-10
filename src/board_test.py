# Test file for board.py

from board import GameBoard
from main import test

def runTests():
    testPlaceMove()
    testCheckBounds()


# Tests placeMove function
def testPlaceMove():
    testsPassed = True
    testBoard = GameBoard(5, 5)

    # Test place "x" at (2, 2)
    testBoard.placeMove(2, 2, "x")
    if testBoard.board[2][2] != "x":
        print("Expected 'x' at (2, 2) but did not find one")
        testsPassed = False

    if testsPassed == True:
        print("PlaceMove Tests Passed")

# Tests checkBounds function
def testCheckBounds():
    testsPassed = True
    testBoard = GameBoard(5, 5)
    
    # Row value too high
    rowValHigh = testBoard.checkBounds(7, 4)
    if rowValHigh == True:
        print("Expected error that row value is too high but got none")
        testsPassed = False
    
    # Col value too high
    colValHigh = testBoard.checkBounds(4, 7)
    if colValHigh == True:
        print("Expected error that col value is too high but got none")
        testsPassed = False

    # Row value negative
    rowValNeg = testBoard.checkBounds(-2, 3)
    if rowValNeg == True:
        print("Expected error that row value is negative but got none")
        testsPassed = False

    if testsPassed == True:
        print("CheckBounds Tests Passed")




runTests()