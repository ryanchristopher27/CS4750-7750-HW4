

from board import GameBoard

#node for minimax tree
class Node:
    def __init__(self, gameBoard, move, nextTurn, terminal):
        #state is the current board at the moment
        self.state = GameBoard(gameBoard)
        #the move it takes to get to it's state
        self.move = move
        #player who took the turn (X or O)
        self.nextTurn = nextTurn
        #if the current state is a terminal (too how many moves)
        #state is terminal if terminal=0
        self.terminal = terminal
        #children nodes (all possible moves from current state)
        self.children = []

    #adds the children of the node
    def expand(self):
        #for every open slot in the current state, there is a move that is available for X or O
        #expanding from an X move results in an O move, and vise versa
        for row in range(self.state.rowCount):
            for col in range(self.state.colCount):
                #if a space is open in the current state, fill state space, and add that state with that filled space as a child
                if self.state.board[row][col] == 0:
                    newBoard = GameBoard(self.state)
                    newBoard.board[row][col] = self.nextTurn
                    #state of child has the possible node filled, the move that would get to that state, and is one more move down the tree
                    self.children.append(Node(newBoard, (row, col), self.nextTurn * -1, self.terminal-1))

        
#minimax search
#state = current gameboard
#xo = whos turn it is
#plyCount = number of states to search ahead
#follows psueudocode from slides/book
def minimaxSearch(state, xo, plyCount):

    #root node
    #on first expansion will be of turn xo
    root = Node(state, None, xo, plyCount)
    vMove = maxValueSearch(root)
    return vMove #(value, move)

def maxValueSearch(node):

    if node.terminal == 0:
        return (utility(node), node.move)

    node.expand()
    largest = -1000
    v = -1000
    move = None
    for child in node.children:
        v = minValueSearch(child)[0]
        if v > largest:
            v = largest
            move = child.move
    return (v, move)

def minValueSearch(node):

    if node.terminal == 0:
        return (utility(node), node.move)

    node.expand()
    smallest = 1000
    v = 1000
    move = None
    for child in node.children:
        v = maxValueSearch(child)[0]
        if v < smallest:
            v = smallest
            move = child.move
    return (v, move)

#calculates the hueristic using a gameboard and who is interested (X or O)
def utility(node):
    gameBoard = node.state
    xo = node.nextTurn * -1
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







    




    
    
    
