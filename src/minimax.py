

from board import GameBoard

#node for minimax tree
class Node:
    def __init__(self, gameBoard, move, currentPlayer, movesLeft):
        #state is the current board at the moment
        self.state = gameBoard
        #the move it takes to get to it's state
        self.move = move
        #player who took the turn (X or O)
        self.currentPlayer = currentPlayer
        #number of moves left (tracking depth)
        self.movesLeft = movesLeft
        #children nodes (all possible moves from current state)
        self.children = []


    # returns col location 
    def checkPieceNextToColCheck(self, col):
        # col value is not on either side
        if col != 0 and col != self.state.colCount - 1:
            return "mid"
        # col value is on right side
        elif col == 0:
            return "left"
        # col value is on left side
        else:
            return "right"

    # returns row location
    def checkPieceNextToRowCheck(self, row):
        # row value is not on top or bottom
        if row != 0 and row != self.state.rowCount - 1:
            return "mid"
        # row value is on top
        elif row == 0:
            return "top"
        # row value is on bottom
        else:
            return "bot"

    # Check all possible 8 boxes around current location if there is a piece placed next to it
    def hasPieceNextTo(self, row, col):
        # checks if row is not on top or bottom row
        rowLoc = self.checkPieceNextToRowCheck(row)
        colLoc = self.checkPieceNextToColCheck(col)

        # top left
        if rowLoc != "top" and colLoc != "left":
            if self.state.board[row-1][col-1] != "-":
                return True
        # top mid
        if rowLoc != "top":
            if self.state.board[row-1][col] != "-":
                return True
        # top right
        if rowLoc != "top" and colLoc != "right":
            if self.state.board[row-1][col+1] != "-":
                return True
        # middle left
        if colLoc != "left":
            if self.state.board[row][col-1] != "-":
                return True
        # middle right
        if colLoc != "right":
            if self.state.board[row][col+1] != "-":
                return True
        # bottom left
        if rowLoc != "bot" and colLoc != "left":
            if self.state.board[row+1][col-1] != "-":
                return True
        # bottom middle
        if rowLoc != "bot":
            if self.state.board[row+1][col] != "-":
                return True
        # bottom right
        if rowLoc != "bot" and colLoc != "right":
            if self.state.board[row+1][col+1] != "-":
                return True

        return False


    #adds the children of the node
    def expand(self):
        #for every open slot in the current state, there is a move that is available for X or O
        #expanding from an X move results in an O move, and vise versa
        for row in range(self.state.rowCount):
            for col in range(self.state.colCount):
                #if a space is open in the current state, fill state space, and add that state with that filled space as a child
                # if self.state.board[row][col] == 0:
                if self.hasPieceNextTo(row, col) and self.state.board[row][col] == "-":
                    newBoard = GameBoard(self.state.rowCount, self.state.colCount)
                    newBoard.setNewBoard(self.state)
                    # newBoard = GameBoard(self.state)
                    newBoard.placeMove(row, col, self.currentPlayer)
                    # newBoard.board[row][col] = self.currentPlayer
                    #state of child has the possible node filled, the move that would get to that state, and is one more move down the tree
                    if self.currentPlayer == "x":
                        self.children.append(Node(newBoard, (row, col), "o", self.movesLeft-1))
                    else:
                        self.children.append(Node(newBoard, (row, col), "x", self.movesLeft-1))   

# smallest col and then smallest row
# gets all moves with same score and breaks the tie
# function works
def tieBreakMoves(moves):
    smallestCols = []
    smallestCol = moves[0][1]
    for move in moves:
        if move[1] == smallestCol:
            smallestCols.append(move)
        elif move[1] < smallestCol:
            smallestCols.clear()
            smallestCols.append(move)
            smallestCol = move[1]

    bestMove = ()
    bestMove = smallestCols[0]
    if len(smallestCols) > 1:
        bestMove = smallestCols[0]
        smallestRow = smallestCols[0][0]
        for i in smallestCols:
            if i[0] < smallestRow:
                bestMove = i
    # else:
    #     bestMove = smallestCols

    return bestMove
    
    # rootNode.movesLeft = rootNode.movesLeft - 1
        
#minimax search
#state = current gameboard
#xo = whos turn it is
#plyCount = number of states to search ahead
#follows psueudocode from slides/book
def minimaxSearch(state, xo, plyCount):

    #root node
    #on first expansion will be of turn xo
    root = Node(state, None, xo, plyCount)
    vMove = findBestMove(root)
    state.placeMove(vMove[0], vMove[1], xo)
    # return (vMove[0], vMove[1].move)
    return vMove #(value, move)

def minimax(node, isMax):

    #checking if there is a winner and if there are moves left
    if node.state.winner == "x" or node.state.winner == "o":
        if node.state.winner == node.currentPlayer:
        # if node.state.winner == node.nextTurn * -1:
            return -1000
        elif node.state.winner != node.currentPlayer:
            return 1000
    
    if node.movesLeft == 0:
        # return (utility(node), node.move) 
        # print(node.move, " ", utility(node))
        return utility(node)
        
    # while(node.movesLeft != 0):
    if isMax:
        best = -1000
        node.expand()
        for child in node.children:
            best = max(best, minimax(child, not isMax))
            # best = max(best, minimax(child, not isMax))
        # print(best, " best")
        return best
    else :
        best = 1000
        node.expand()
        for child in node.children:
            # minimax(child, not isMax)
            best = min(best, minimax(child, not isMax))
        # print(best, " best")
        return best

def findBestMove(node) :
    bestVal = -100
    bestMove = (-1,-1)
    moves = []

    node.expand()
    for child in node.children:
        moveVal = minimax(child, False) 

        if moveVal > bestVal :
            # bestMove = child.move
            bestVal = moveVal
            moves = []
            moves.append(child.move)
        if moveVal == bestVal:
            moves.append(child.move)

    # tie break all moves with smallest value
    if len(moves) > 1:
        bestMove = tieBreakMoves(moves)

    return bestMove

# def maxValueSearch(node):

#     if node.state.terminal == True:
#         if node.state.winner == "x" or node.state.winner == "o":
#             if node.state.winner != node.nextTurn:
#             # if node.state.winner == node.nextTurn * -1:
#                 return -1000
#             elif node.state.winner == node.nextTurn:
#                 return 1000
#         else:
#             return 0

#     if node.movesLeft == 0:
#         return (utility(node), node.move)

#     #current move
#     node.expand()

#     #has to expand all possible moves before looking at hursitc values
#     currentNode = node.children
#     while(node.movesLeft != 0):
#         for children in currentNode:
#             child.expend


#     largest = -1000
#     v = -1000
#     moves = []
#     move = None
#     for child in node.children:
#         child.expand()
        # v = minValueSearch(child)[0]
        # child.state.determineMove(child.currentPlayer)
        # v = utility(child.state)
        # v = maxValueSearch(child.state)
        # if v > largest:
        #     v = largest
        #     move = child.move
            # move = child

        # if v >= largest:
        #     v = largest
        #     moves.append(child.move)

    # tie break all moves with smallest value
    # if len(moves) > 1:
    #     move = tieBreakMoves(moves)
    # else:
    #     move = moves

    # return (v, move)
    # return (v, child)

# def minValueSearch(node):

#     if node.state.terminal == True:
#         if node.state.winner == "x" or node.state.winner == "o":
#             if node.state.winner != node.nextTurn:
#             # if node.state.winner == node.nextTurn * -1:
#                 return -1000
#             elif node.state.winner == node.nextTurn:
#                 return 1000
#          else:
    #         return 0

    # if node.movesLeft == 0:
    #     return (utility(node), node.move)

    # node.expand()
    # smallest = 1000
    # v = 1000
    # move = None
    # moves = []
    # for child in node.children:
    #     v = maxValueSearch(child)[0]
    #     # child.state.determineMove(child.currentPlayer)
    #     # v = utility(maxValueSearch(child.state))
    #     # if v < smallest:
    #     #     v = smallest
    #     #     move = child.move
    #     if v <= smallest:
    #         v = smallest
    #         moves.append(child.move)

    # # tie break all moves with smallest value
    # if len(moves) > 1:
    #     move = tieBreakMoves(moves)
    # else:
    #     move = moves

    # return (v, move)

#calculates the hueristic using a gameboard and who is interested (X or O)
def utility(node):
    gameBoard = node.state
    gameBoard.determineMove(node.currentPlayer)
    # xo = node.nextTurn * -1
    # xo = "x"
    # if node.currentPlayer == "x":
    #     xo = "o"

    hn = 0
    # if xo == 1:
    # if xo == "x":
    if node.currentPlayer == "x":
        hn += 200*(gameBoard.twoSideOpen3forX) - 80*(gameBoard.twoSideOpen3forO)
        hn += 150*(gameBoard.oneSideOpen3forX) - 40*(gameBoard.oneSideOpen3forO)
        hn += 20*(gameBoard.twoSideOpen2forX) - 15*(gameBoard.twoSideOpen2forO)
        hn += 5*(gameBoard.oneSideOpen2forX) - 2*(gameBoard.oneSideOpen2forO)
    else:
        hn += 200*(gameBoard.twoSideOpen3forO) - 80*(gameBoard.twoSideOpen3forX)
        hn += 150*(gameBoard.oneSideOpen3forO) - 40*(gameBoard.oneSideOpen3forX)
        hn += 20*(gameBoard.twoSideOpen2forO) - 15*(gameBoard.twoSideOpen2forX)
        hn += 5*(gameBoard.oneSideOpen2forO) - 2*(gameBoard.oneSideOpen2forX)
    return hn

def testExpandNodes():
    state = GameBoard(5,4)
    state.placeMove(1,1,'x')
    state.placeMove(0,1, 'x')
    state.placeMove(1,0,'x')
    state.placeMove(0,0, 'o')
    state.placeMove(3,3, 'o')

    root = Node(state, None, 'x', 3)
    bestMove = findBestMove(root)
    # print(bestMove)
    # root.expand()
    # expandLookAhead(root)



    
    
# testExpandNodes()