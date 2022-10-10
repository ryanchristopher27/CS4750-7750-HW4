class GameBoard:

    def __init__(self, rowCount, colCount):

        self.winner = 0

        self.terminal = False

        self.openMoves = rowCount * colCount

        self.rowCount = rowCount
        self.colCount = colCount
        self.board = [[0]*colCount]*rowCount

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
    def __init__(self, gameBoard):

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


    #places an X or O on the board then determines what it means
    def placeMove(self, row, col, xo):
        self.board[row][col] = xo
        self.determineMove(xo)
        self.openMoves -=1
        if self.openMoves <= 0:
            self.terminal = True

    #this determins how many openings are on the board for either X or O player and determines a winner if there is one
    def determineMove(self, xo):
        if self.winner != 0:
            self.checkRow(xo)
        if self.winner != 0:
            self.checkCol(xo)
        if self.winner != 0:
            self.checkDiag1(xo)
        if self.winner != 0:
            self.checkDiag2(xo)


    #checks the bounds of the indexes to make sure they are legal
    def checkBounds(self, row, col):
        rowInBounds = False
        colInBounds = False
        if row < self.rowCount or row >= 0:
            rowInBounds = True
        if col < self.colCount or col >=0:
            colInBounds = True
        if rowInBounds and colInBounds:
            return True
        else:
            return False
    

    #determines who (X or O) to add a one or two open sided pairing that is either 2 or 3 spaces long for either X or O
    #helper function for changeOpenings()
    def addSideOpen(self, xo, numConsec, oneOrTwo):
        #if player X
        if xo == 1:
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
        keepsGoing = False

        #determines number of consecutive X's or O's
        numConsec = 0

        #determines if the left side (or north side) of the pattern is open
        leftOpen = False

        #determines if the right side (or south side) of the pattern is open
        rightOpen = False


        #checking row by row for horizontal patterns
        for row in range(self.rowCount):

            #walking through the row
            for col in range(self.colCount):

                #if the pattern matches
                if self.board[row][col] == xo:
                    numConsec += 1

                #if the number of consecutive X's or O's in a pattern is 4, then they are a winner
                if numConsec >= 4:
                    self.winner = xo
                    return

                #if there is a pattern
                if numConsec >= 2:
                    
                    #if bounds are legal, check them
                    if self.checkBounds(row, col + 1):

                        #if the next box is of matching pattern, do not count this as a 2 or 3 in a row...yet
                        if self.board[row][col+1] == xo:
                            keepsGoing = True

                        #check the next box. If it is open, then mark it
                        elif self.board[row][col + 1] == 0:
                            rightOpen = True

                    #check behind the consecutive pattern to see if it is open
                    if self.checkBounds(row, col - numConsec):
                        if self.board[row][col - numConsec] == 0:
                            leftOpen = True

                    #if the next box isn't of matching type (if the pattern doesn't continue) mark it down
                    if keepsGoing == False:

                        #if the left and right are open, then two sided open
                        if rightOpen and leftOpen:
                            self.addSideOpen(xo, numConsec, 2)
                        
                        #else if just the left or just the right, then it is one sided open
                        elif rightOpen or leftOpen:
                            self.addSideOpen(xo, numConsec, 1)


# ****
# NOTE!!!!!!!
# the following three searches follow the same logic as above for column vertical search and diagnal search
# ****

#see checkRow() for more detailed comments
    def checkCol(self, xo):
        keepsGoing = False
        numConsec = 0
        topOpen = False
        bottomOpen = False
        #checking column by column for vertical patterns
        for col in range(self.colCount):
            for row in range(self.rowCount):

                if self.board[row][col] == xo:
                    numConsec += 1

                if numConsec >= 4:
                    self.winner = xo
                    return

                if numConsec >= 2:
                    if self.checkBounds(row + 1, col):
                        if self.board[row+1][col] == xo:
                            keepsGoing == True
                        elif self.board[row + 1][col] == 0:
                            bottomOpen = True

                    if self.checkBounds(row - numConsec, col):
                        if self.board[row - numConsec][col] == 0:
                            topOpen = True

                    if keepsGoing == False:
                        if topOpen and bottomOpen:
                            self.addSideOpen(xo, numConsec, 2)
                        elif topOpen or bottomOpen:
                            self.addSideOpen(xo, numConsec, 1)

#see checkRow() for more detailed comments
    def checkDiag1(self, xo):
        keepsGoing = False
        numConsec = 0
        leftOpen = False
        rightOpen = False
        #checking for diagnal patterns top left to bottom right
        for row in range(self.rowCount):
            for i in range(row, self.rowCount if self.rowCount > self.colCount else self.colCount):

                if self.board[i][i] == xo:
                    numConsec += 1

                if numConsec >= 4:
                    self.winner = xo
                    return

                if numConsec >= 2:
                    if self.checkBounds(i+1, i+1):
                        if self.board[i+1][i+1] == xo:
                            keepsGoing = True
                        elif self.board[i + 1][i + 1] == 0:
                            rightOpen = True

                    if self.checkBounds(i - numConsec, i - numConsec):
                        if self.board[i - numConsec][i - numConsec] == 0:
                            leftOpen = True

                    if keepsGoing == False:
                        if rightOpen and leftOpen:
                            self.addSideOpen(xo, numConsec, 2)
                        elif rightOpen or leftOpen:
                            self.addSideOpen(xo, numConsec, 1)
            
#see checkRow() for more detailed comments
    def checkDiag2(self, xo):
        keepsGoing = False
        numConsec = 0
        leftOpen = False
        rightOpen = False
        #checking for horizontal patterns bottom left to top right
        for row in range(self.rowCount):
            for i in range(row, self.rowCount if self.rowCount > self.colCount else self.colCount):

                #starting at the bottom of the row
                j = self.rowCount-1 - i
                if self.board[j][i] == xo:
                    numConsec += 1

                if numConsec >= 4:
                    self.winner = xo
                    return

                if numConsec >= 2:
                    if self.checkBounds(j-1, i+1):
                        if self.board[j-1][i+1] == xo:
                            keepsGoing = True
                        elif self.board[j-1][i+1] == 0:
                            rightOpen = True

                    if self.checkBounds(j + numConsec, i - numConsec):
                        if self.board[j + numConsec][i - numConsec] == 0:
                            leftOpen = True

                    if keepsGoing == False:
                        if rightOpen and leftOpen:
                            self.addSideOpen(xo, numConsec, 2)
                        elif rightOpen or leftOpen:
                            self.addSideOpen(xo, numConsec, 1)
        


