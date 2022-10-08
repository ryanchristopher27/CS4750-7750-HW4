

from board import GameBoard


#calculates the hueristic using a gameboard and who is interested (X or O)
def calculateHn(gameBoard, xo):
    hn = 0
    if xo == 1:
        hn += 200*(gameBoard.twoSideOpen3forX) - 80*(gameBoard.twoSideOpen3forO)
        hn += 150*(gameBoard.oneSideOpen3forX) - 40*(gameBoard.oneSideOpen3forO)
        hn += 20*(gameBoard.twoSideOpen2forX) - 15*(gameBoard.twoSideOpen2forO)
        hn += 5*(gameBoard.oneSideOpen2forX) - 2*(gameBoard.oneSideOpen2forO)
    else:
        hn += 200*(gameBoard.twoSideOpen3for0) - 80*(gameBoard.twoSideOpen3forX)
        hn += 150*(gameBoard.oneSideOpen3for0) - 40*(gameBoard.oneSideOpen3forX)
        hn += 20*(gameBoard.twoSideOpen2for0) - 15*(gameBoard.twoSideOpen2forX)
        hn += 5*(gameBoard.oneSideOpen2for0) - 2*(gameBoard.oneSideOpen2forX)
    return hn

#node class
#unfinished expand()
class Node:
    def __init__(self, gameBoard, move, minOrMax, parent):
        self.state = GameBoard(gameBoard)
        self.move = move
        self.terminal = True if gameBoard.winner == 0 else False
        self.minOrMax = minOrMax
        self.hn = -1000 if minOrMax == True else 1000 
        self.children = []
        self.parent = parent
        self.depth = parent.depth + 1

    #unfinished
    def expand(self):
        for row in range(self.state.rowCount):
            for col in range(self.state.colCount):
                if self.state.board[row][col] == 0:
                    newBoard = GameBoard(self.state)
                    newBoard.board[row][col] = self.xo
                    self.children.append(Node(newBoard, (row, col), False if self.minOrMax == True else False, self))

        


#whoami is the starting node who originally calls the function (player X or player O)- allows for min and max switching - 
#maxOrMin is the level currently at - True = Max, False = min
#recursively finds the best move for the current node 
#UNFINISHED
def minimaxSearch(node, maxDepth, maxOrMin, whoami):

    score = 0
    move = (0,0)

    if node.depth < maxDepth:
        node.expand()
        smallest = 10000
        largest = -10000
        v = 0
        for child in node.children:
            minimaxSearch(child, maxDepth-1, False if maxOrMin == True else True)
            if maxOrMin == True:
                v = calculateHn(child.state, whoami)
            else: 
                v = calculateHn(child.state, whoami * -1)
            
            if v < smallest:
                smallest = v
            if v > largest:
                largest = v
        node.score = (largest if maxOrMin == True else smallest)
        node.move = node.move






    




    
    
    
