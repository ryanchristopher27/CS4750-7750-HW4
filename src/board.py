class GameBoard(object):

    def __init__(self, rowCount, colCount):

        self.winner = 0

        self.terminal = False

        self.openMoves = rowCount * colCount

        self.rowCount = rowCount
        self.colCount = colCount

        # self.board = [[0]*colCount]*rowCount
        # Board is now initialized with '-' instead of 0
        self.board = [['-' for i in range(colCount)] for j in range(rowCount)]

        #visible for both players to see -> each player should be able to see the following on the board and not have to calculate it
        self.twoSideOpen3forX = 0
        self.twoSideOpen3forO = 0

        self.oneSideOpen3forX = 0
        self.oneSideOpen3forO = 0

        self.twoSideOpen2forX = 0
        self.twoSideOpen2forO = 0

        self.oneSideOpen2forX = 0
        self.oneSideOpen2forO = 0

    #second initializer to create one game board from another
    def setNewBoard(self, gameBoard):

        self.winner = gameBoard.winner

        self.rowCount = gameBoard.rowCount
        self.colCount = gameBoard.colCount
        
        for row in range(gameBoard.rowCount):
            for col in range(gameBoard.colCount):
                self.board[row][col] = gameBoard.board[row][col]


        self.twoSideOpen3forX = gameBoard.twoSideOpen3forX
        self.twoSideOpen3forO = gameBoard.twoSideOpen3forO

        self.oneSideOpen3forX = gameBoard.oneSideOpen3forX
        self.oneSideOpen3forO = gameBoard.oneSideOpen3forO

        self.twoSideOpen2forX = gameBoard.twoSideOpen2forX
        self.twoSideOpen2forO = gameBoard.twoSideOpen2forO

        self.oneSideOpen2forX = gameBoard.oneSideOpen2forX
        self.oneSideOpen2forO = gameBoard.oneSideOpen2forO

    def printBoard(self):
        print("--- Current Game Board ---")
        for row in self.board:
            print(row)

    def clearSideOpens(self):
        self.twoSideOpen3forX = 0
        self.twoSideOpen3forO = 0
        self.oneSideOpen3forX = 0
        self.oneSideOpen3forO = 0
        self.twoSideOpen2forX = 0
        self.twoSideOpen2forO = 0
        self.oneSideOpen2forX = 0
        self.oneSideOpen2forO = 0

    def resetMove(self, row, col):
        self.board[row][col] = '-'
    #places an X or O on the board then determines what it means
    def placeMove(self, row, col, xo):
        self.board[row][col] = xo
        # print("Symbol [", xo, "] placed at Row:", row, "Col:", col)
        self.determineMove(xo)

        # Decrements total spaces in board and checks if board is full
        self.openMoves -= 1
        # print("Number of open moves:", self.openMoves)
        if self.openMoves <= 0:
            self.terminal = True

    #this determins how many openings are on the board for either X or O player and determines a winner if there is one
    def determineMove(self, xo):
        self.clearSideOpens()
        if self.winner == 0:
            self.checkRow(xo)
        if self.winner == 0:
            self.checkCol(xo)
        # if self.winner == 0:
        #     self.checkDiag1(xo)
        # if self.winner == 0:
        #     self.checkDiag2(xo)
        if self.winner == 0:
            self.newDiag1Check(xo)
        if self.winner == 0:
            self.newDiag2Check(xo)
        if self.winner == 0:
            self.newDiag3Check(xo)
        if self.winner == 0:
            self.newDiag4Check(xo)  


    #checks the bounds of the indexes to make sure they are legal
    def checkBounds(self, row, col):
        rowInBounds = False
        colInBounds = False
        if row < self.rowCount and row >= 0:
            rowInBounds = True
        if col < self.colCount and col >=0:
            colInBounds = True
        if rowInBounds and colInBounds:
            return True
        else:
            return False
    

    #determines who (X or O) to add a one or two open sided pairing that is either 2 or 3 spaces long for either X or O
    #helper function for changeOpenings()
    def addSideOpen(self, xo, numConsec, oneOrTwo):
        #if player X
        # if xo == 1:
        if xo == "x":
            #if two consecutive X's
            if numConsec == 2:
                #if one open side
                if oneOrTwo == 1:
                    self.oneSideOpen2forX += 1
                #else two open sides
                else:
                    self.twoSideOpen2forX += 1
            #else three consecutive X's
            else:
                #if one open side
                if oneOrTwo == 1:
                    self.oneSideOpen3forX += 1
                #else two open sides
                else:
                    self.twoSideOpen3forX += 1
        #else player O
        else:
            #if two consecutive O's
            if numConsec == 2:
                if oneOrTwo == 1:
                    self.oneSideOpen2forO += 1
                else:
                    self.twoSideOpen2forO += 1
            #else three consecutive 0's
            else:
                #if one open side
                if oneOrTwo == 1:
                    self.oneSideOpen3forO += 1
                #else two open sides
                else:
                    self.twoSideOpen3forO += 1


    def checkRow(self, xo):
        #determines if the next box is of matching type
        keepsGoing = True

        #determines number of consecutive X's or O's
        numConsec = 0

        #determines if the left side (or north side) of the pattern is open
        leftOpen = False

        #determines if the right side (or south side) of the pattern is open
        rightOpen = False


        #checking row by row for horizontal patterns
        for row in range(self.rowCount):
            leftOpen = False
            #walking through the row
            for col in range(self.colCount):

                #if the pattern matches
                if self.board[row][col] == xo:
                    numConsec += 1
                else:
                    numConsec = 0

                if numConsec >= 4:
                    self.winner = xo
                    return

                #if there is a pattern
                if numConsec >= 2:
                    
                    #if bounds are legal, check them
                    if self.checkBounds(row, col + 1):

                        #if the next box is of matching pattern, do not count this as a 2 or 3 in a row...yet
                        if self.board[row][col+1] != xo:
                            keepsGoing = False
                            #check the next box. If it is open, then mark it
                            if self.board[row][col + 1] == "-":
                                rightOpen = True
                    
                    else:
                        #takes care of edge cases
                        keepsGoing = False 

                    #check behind the consecutive pattern to see if it is open
                    if self.checkBounds(row, col - numConsec):
                        if self.board[row][col - numConsec] == "-":
                            leftOpen = True

                    #if the next box isn't of matching type (if the pattern doesn't continue) mark it down
                    if keepsGoing == False:

                        #if the left and right are open, then two sided open
                        if rightOpen and leftOpen:
                            self.addSideOpen(xo, numConsec, 2)
                        
                        #else if just the left or just the right, then it is one sided open
                        elif rightOpen or leftOpen:
                            self.addSideOpen(xo, numConsec, 1)
                        numConsec = 0
            numConsec = 0


# ****
# NOTE!!!!!!!
# the following three searches follow the same logic as above for column vertical search and diagnal search
# ****

#see checkRow() for more detailed comments
    def checkCol(self, xo):
        keepsGoing = True
        numConsec = 0
        topOpen = False
        bottomOpen = False
        #checking column by column for vertical patterns
        for col in range(self.colCount):
            topOpen = False
            for row in range(self.rowCount):

                if self.board[row][col] == xo:
                    numConsec += 1
                else:
                   numConsec = 0

                if numConsec >= 4:
                    self.winner = xo
                    return 

                if numConsec >= 2:
                    if self.checkBounds(row + 1, col):
                        if self.board[row+1][col] != xo:
                            keepsGoing = False
                            # elif self.board[row + 1][col] == 0:
                            if self.board[row + 1][col] == "-":
                                bottomOpen = True
                    else: 
                        keepsGoing = False

                    if self.checkBounds(row - numConsec, col):
                        if self.board[row - numConsec][col] == "-":
                            topOpen = True

                    if keepsGoing == False:
                        if topOpen and bottomOpen:
                            self.addSideOpen(xo, numConsec, 2)
                        elif topOpen or bottomOpen:
                            self.addSideOpen(xo, numConsec, 1)
                        numConsec = 0
            numConsec = 0

    # Checks top-left half from bottom left to top right for each possible diagonal
    def newDiag1Check(self, xo):
        keepsGoing = False
        numConsec = 0
        leftDownOpen = False
        rightUpOpen = False

        for rowCount in range(2, self.rowCount - 1):
            col = 0
            row = rowCount
            while col <= row and row <= self.colCount - 1:
                #if the pattern matches
                if self.board[row][col] == xo:
                    numConsec += 1

                if numConsec >= 4:
                    self.winner = xo
                    return
                
                if numConsec >= 2:
                    if self.checkBounds(row - 1, col + 1):
                        if self.board[row - 1][col + 1] == xo:
                            keepsGoing = True
                        else:
                            keepsGoing = False
                            if self.board[row - 1][col + 1] == "-":
                                rightUpOpen = True

                            if self.checkBounds(row + numConsec, col - numConsec):
                                if self.board[row + numConsec][col - numConsec] == "-":
                                    leftDownOpen = True
                    
                    #if the next box isn't of matching type (if the pattern doesn't continue) mark it down
                    if keepsGoing == False:
                        #if the left and right are open, then two sided open
                        if rightUpOpen and leftDownOpen:
                            self.addSideOpen(xo, numConsec, 2)
                        
                        #else if just the left or just the right, then it is one sided open
                        elif rightUpOpen or leftDownOpen:
                            self.addSideOpen(xo, numConsec, 1)
                        numConsec = 0
                row -= 1
                col += 1
            numConsec = 0

    # Checks bottom-right half from bottom left to top right for each possible diagonal
    def newDiag2Check(self, xo):
        keepsGoing = False
        numConsec = 0
        leftDownOpen = False
        rightUpOpen = False

        for colCount in range(1, self.colCount - 2):

            col = colCount
            row = self.rowCount - 1
            while col <= self.colCount - 1 and row >= 0:
                #if the pattern matches
                if self.board[row][col] == xo:
                    numConsec += 1

                if numConsec >= 4:
                    self.winner = xo
                    return
                
                if numConsec >= 2:
                    if self.checkBounds(row - 1, col + 1):
                        if self.board[row - 1][col + 1] == xo:
                            keepsGoing = True
                        else:
                            keepsGoing = False
                            if self.board[row - 1][col + 1] == "-":
                                rightUpOpen = True

                            if self.checkBounds(row + numConsec, col - numConsec):
                                if self.board[row + numConsec][col - numConsec] == "-":
                                    leftDownOpen = True
                    
                    #if the next box isn't of matching type (if the pattern doesn't continue) mark it down
                    if keepsGoing == False:
                        #if the left and right are open, then two sided open
                        if rightUpOpen and leftDownOpen:
                            self.addSideOpen(xo, numConsec, 2)
                        
                        #else if just the left or just the right, then it is one sided open
                        elif rightUpOpen or leftDownOpen:
                            self.addSideOpen(xo, numConsec, 1)
                        numConsec = 0
                row -= 1
                col += 1
            numConsec = 0
            
    # Checks bottom-left half from top left to bottom right for each possible diagonal
    def newDiag3Check(self, xo):
        keepsGoing = False
        numConsec = 0
        leftUpOpen = False
        rightDownOpen = False

        for rowCount in range(self.rowCount - 1):

            col = 0
            row = rowCount
            while col <= self.colCount - 1 and row <= self.rowCount - 1:
                #if the pattern matches
                if self.board[row][col] == xo:
                    numConsec += 1

                if numConsec >= 4:
                    self.winner = xo
                    return
                
                if numConsec >= 2:
                    if self.checkBounds(row + 1, col + 1):
                        if self.board[row + 1][col + 1] == xo:
                            keepsGoing = True
                        else:
                            keepsGoing = False
                            if self.board[row + 1][col + 1] == "-":
                                rightDownOpen = True

                            if self.checkBounds(row - numConsec, col - numConsec):
                                if self.board[row - numConsec][col - numConsec] == "-":
                                    leftUpOpen = True
                    
                    #if the next box isn't of matching type (if the pattern doesn't continue) mark it down
                    if keepsGoing == False:
                        #if the left and right are open, then two sided open
                        if rightDownOpen and leftUpOpen:
                            self.addSideOpen(xo, numConsec, 2)
                        
                        #else if just the left or just the right, then it is one sided open
                        elif rightDownOpen or leftUpOpen:
                            self.addSideOpen(xo, numConsec, 1)

                        numConsec = 0
                row += 1
                col += 1
            numConsec = 0

    # Checks top-right half from top left to bottom right for each possible diagonal
    def newDiag4Check(self, xo):
        keepsGoing = False
        numConsec = 0
        leftUpOpen = False
        rightDownOpen = False

        for colCount in range(1, self.colCount - 2):

            col = colCount
            row = 0
            while col <= self.colCount - 1 and row <= self.rowCount - 1:
                #if the pattern matches
                if self.board[row][col] == xo:
                    numConsec += 1

                if numConsec >= 4:
                    self.winner = xo
                    return
                
                if numConsec >= 2:
                    if self.checkBounds(row + 1, col + 1):
                        if self.board[row + 1][col + 1] == xo:
                            keepsGoing = True
                        else:
                            keepsGoing = False
                            if self.board[row + 1][col + 1] == "-":
                                rightDownOpen = True

                            if self.checkBounds(row - numConsec, col - numConsec):
                                if self.board[row - numConsec][col - numConsec] == "-":
                                    leftUpOpen = True
                    
                    #if the next box isn't of matching type (if the pattern doesn't continue) mark it down
                    if keepsGoing == False:
                        #if the left and right are open, then two sided open
                        if rightDownOpen and leftUpOpen:
                            self.addSideOpen(xo, numConsec, 2)
                        
                        #else if just the left or just the right, then it is one sided open
                        elif rightDownOpen or leftUpOpen:
                            self.addSideOpen(xo, numConsec, 1)
                        numConsec = 0
                row += 1
                col += 1
            numConsec = 0
