# Test file for board.py

from board import GameBoard
from main import test

def runTests():
    # testPlaceMove()
    # testCheckBounds()
    # testaddSideOpen()
    testCheckRow()
    # testCheckCol()


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


def testaddSideOpen():
    testsPassed = True
    testBoard = GameBoard (5,5)

    testBoard.addSideOpen('x', 3, 1)
    if(testBoard.oneSideOpen3forX != 1):
        print("Expected 1 for oneSideOpen3forX, and got ", testBoard.oneSideOpen3forX)
        testsPassed = False

    testBoard.addSideOpen('x', 3, 2)
    if(testBoard.twoSideOpen3forX != 1):
        print("Expected 1 for twoSideOpen3forX, and got ", testBoard.twoSideOpen3forX)
        testsPassed = False

    testBoard.addSideOpen('x', 2, 1)
    if(testBoard.oneSideOpen2forX != 1):
        print("Expected 1 for oneSideOpen2forX, and got ", testBoard.oneSideOpen2forX)
        testsPassed = False
    
    testBoard.addSideOpen('x', 2, 2)
    if(testBoard.twoSideOpen2forX != 1):
        print("Expected 1 for twoSideOpen2forX, and got ", testBoard.twoSideOpen2forX)
        testsPassed = False

    testBoard.addSideOpen('o', 2, 1)
    if(testBoard.oneSideOpen2forO != 1):
        print("Expected 1 for oneSideOpen2forO, and got ", testBoard.oneSideOpen2forO)
        testsPassed = False
    
    testBoard.addSideOpen('o', 2, 2)
    if(testBoard.twoSideOpen2forO != 1):
        print("Expected 1 for twoSideOpen2forO, and got ", testBoard.twoSideOpen2forO)
        testsPassed = False
    
    testBoard.addSideOpen('o', 3, 1)
    if(testBoard.oneSideOpen3forO != 1):
        print("Expected 1 for oneSideOpen3forO, and got ", testBoard.oneSideOpen3forO)
        testsPassed = False

    testBoard.addSideOpen('o', 3, 2)
    if(testBoard.twoSideOpen3forO != 1):
        print("Expected 1 for twoSideOpen3forO, and got ", testBoard.twoSideOpen3forO)
        testsPassed = False

    if testsPassed == True:
        print("addSideOpen Tests Passed")    

def testCheckRow():
    testsPassed = True
    testBoard = GameBoard (5,5)

    #generic test
    testBoard.placeMove(4,2, 'x')
    testBoard.placeMove(4,3, 'x')
    # testBoard.checkRow('x')
    testBoard.printBoard()
    if(testBoard.twoSideOpen2forX != 1):
        print("Expected 1 for twoSideOpen2forX, and got ", testBoard.twoSideOpen2forX)
        testsPassed = False

    #right edge case
    testBoard.placeMove(4,4, 'x')
    testBoard.clearSideOpens()
    testBoard.checkRow('x')
    testBoard.printBoard()
    if(testBoard.oneSideOpen3forX != 1):
        print("Expected 1 for oneSideOpen3forX, and got ", testBoard.oneSideOpen3forX)
        testsPassed = False
    
    #check winnder
    testBoard.placeMove(4,1, 'x')
    testBoard.checkRow('x')
    testBoard.clearSideOpens()
    if(testBoard.winner != 'x'):
        print("Expected 'x' as winner and got", testBoard.winner)
        testsPassed = False

    #left edge case
    testBoard.placeMove(4, 0, 'x')
    testBoard.placeMove(4, 3, '-')
    testBoard.checkRow('x')
    if(testBoard.oneSideOpen3forX != 1):
        print("Expected 1 for oneSideOpen3forX, and got ", testBoard.oneSideOpen3forX)
        testsPassed = False

    if(testsPassed == True):
        print("checkRow Tests Passed")
        testsPassed = False

def testCheckCol():
    testsPassed = True
    testBoard = GameBoard (5,5)
    #generic test
    testBoard.placeMove(2,4, 'x')
    testBoard.placeMove(3,4, 'x')
    testBoard.printBoard()
    testBoard.checkCol('x')
    if(testBoard.twoSideOpen2forX != 1):
        print("Expected 1 for twoSideOpen2forX, and got ", testBoard.twoSideOpen2forX)
        testsPassed = False

    #down edge case
    testBoard.placeMove(4,4, 'x')
    testBoard.clearSideOpens()
    testBoard.checkCol('x')
    if(testBoard.oneSideOpen3forX != 1):
        print("Expected 1 for oneSideOpen3forX, and got ", testBoard.oneSideOpen3forX)
        testsPassed = False
    
    #check winner
    testBoard.placeMove(1,4, 'x')
    testBoard.checkCol('x')
    testBoard.clearSideOpens()
    if(testBoard.winner != 'x'):
        print("Expected 'x' as winner and got", testBoard.winner)
        testsPassed = False

    #top edge case
    testBoard.placeMove(0, 4, 'x')
    testBoard.placeMove(3, 4, '-')
    testBoard.checkRow('x')
    testBoard.printBoard()

    if(testBoard.oneSideOpen3forX != 1):
        print("Expected 1 for oneSideOpen3forX, and got ", testBoard.oneSideOpen3forX)
        testsPassed = False
    # testBoard.placeMove(4, 4, '-')
    print("testBoard.oneSideOpen3forX", testBoard.oneSideOpen3forX)
    print("testBoard.oneSideOpen2forX", testBoard.oneSideOpen2forX)
    print("testBoard.twoSideOpen3forX", testBoard.twoSideOpen3forX)
    print("testBoard.twoSideOpen2forX", testBoard.twoSideOpen2forX)

    if(testsPassed == True):
        print("checkCol Tests Passed")


runTests()