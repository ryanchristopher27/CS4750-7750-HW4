

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

#node for minimax tree
class Node:
    def __init__(self, gameBoard, move, parent):
        #state is the current board at the moment
        self.state = GameBoard(gameBoard)
        #the move it takes to get to it's state
        self.move = move
        #if the current state is a terminal board (win or loss)
        self.terminal = True if gameBoard.winner == 0 else False
        #hn is null at before it knows what the best move for it's current state
        self.hn = None 
        #children nodes (all possible moves from current state)
        self.children = []
        #parent node
        self.parent = parent
        #determines it's depth for search purposes (2ply vs 4ply etc)
        self.depth = parent.depth + 1

    #adds the children of the node
    def expand(self, xo):
        #for every open slot in the current state, there is a move that is available for X or O
        #expanding from an X move results in an O move, and vise versa
        for row in range(self.state.rowCount):
            for col in range(self.state.colCount):
                #if a space is open in the current state, fill state space, and add that state with that filled space as a child
                if self.state.board[row][col] == 0:
                    newBoard = GameBoard(self.state)
                    newBoard.board[row][col] = xo
                    #state of child has the possible node filled, the move that would get to that state, and is the opposite of it's parent (min or max)
                    self.children.append(Node(newBoard, (row, col), self))

        

def minimaxSearch(state, xo):

    root = Node(state, None, None)
    root.expand(xo)

    move = maxValueSearch(root)

    return move

def maxValueSearch(node):
    #unsure what terminal actually means
    if node.terminal == True:
        return 1000
    
    largest = -1000
    v = -1000
    move = None
    for child in node.children:
        v = minValueSearch(child)
        if v > largest:
            v = largest
            move = child.move
    return (v, move)

def minValueSearch(node):

    #unsure what terminal actually means
    if node.terminal == True:
        return -1000
    smallest = 1000
    v = 1000
    move = None
    for child in node.children:
        v = maxValueSearch(child)
        if v < smallest:
            v = smallest
            move = child.move
    return (v, move)







    




    
    
    
