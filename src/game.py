# game class
from board import GameBoard
from minimax import minimaxSearch
from player import Player

class Game():

    # Attributes
        # Player 1
        # Player 2
        # Gameboard
        # MoveSequence
    
    # Functions:
        # Player 1 Move
        # Player 2 Move
        # Getters and Setters
            # MoveSequence
        # PlayGame
            # Loop between players til terminal is returned by one of players
        # Print Sequence
    moveSequence = []

    def __init__(self, p1MovesAhead, p2MovesAhead, p1FirstMove, p2FirstMove, boardRowSize, boardColSize):
        # generate board    
        print(boardRowSize, " ", boardColSize)
        self.gameboard = GameBoard(boardRowSize, boardColSize)
        
        # set player 1
        self.player1 = Player(p1MovesAhead, "Player 1", "x", p1FirstMove)

        # set player 2
        self.player2 = Player(p2MovesAhead, "Player 2", "o", p2FirstMove)
        
        #place the moves
        self.gameboard.placeMove(p1FirstMove[0], p1FirstMove[1], 'x')
        self.moveSequence.append(p1FirstMove)
        self.gameboard.placeMove(p2FirstMove[0], p2FirstMove[1], 'o')
        self.moveSequence.append(p2FirstMove)

            

    #getters and setters
    def getGameBoard(self):
        return self.gameboard
    
    def getMoveSequence(self):
        return self.moveSequence

    def getPlayer1(self):
        return self.player1

    def getPlayer2(self):
        return self.player2
    
    def addMoveSequence(self, nextMove):
        self.moveSequence.append(nextMove)

    # def printBoard(self):
    #     print("--- Current Game Board ---")
    #     for row in self.gameboard.board:
    #         print(row)



    #logic functions 

    def playGame(self):
        print("Starting Game")

        # while(self.gameboard.terminal == False):
        #     # may have to check after each player moves if terminal is true. 
        #     self.addMoveSequence(minimaxSearch(self.getGameBoard(), self.player1.playerSymbol, self.player1.movesAhead))
        #     self.gameboard.printBoard()
        #     self.addMoveSequence(minimaxSearch(self.getGameBoard(), self.player2.playerSymbol, self.player2.movesAhead))
        #     self.gameboard.printBoard()
        #     #print(self.moveSequence)

        count = 0
        while (self.gameboard.terminal == False):
            if (count % 2) == 0:
                self.addMoveSequence(minimaxSearch(self.getGameBoard(), self.player1.playerSymbol, self.player1.movesAhead))
            else:
                self.addMoveSequence(minimaxSearch(self.getGameBoard(), self.player2.playerSymbol, self.player2.movesAhead))

            count += 1

            print("\n\tRound:", count)
            self.gameboard.printBoard()

        print(self.moveSequence)
        
        if(self.gameboard.winner == 'x'):
            print("Player 1 won the game")
        
        elif(self.gameboard.winner == 'o'):
            print("player 2 won the game")
        
        elif(self.gameboard.winner == 0):
            print("There was a tie")
        
        else:
            print("Something went wrong")

#instructions say [3,4], for player 1, but not accounting for 0
#instctions say [3,3] for player 2, but not accounting for 0
game1 = Game(2, 4, (2,3), (2,2), 5, 6)
print("Hello")
game1.gameboard.printBoard()
# game1.gameboard.placeMove(1, 2, "x")
# game1.gameboard.printBoard()
# game1.gameboard.placeMove(2, 1, "o")
# game1.gameboard.printBoard()
game1.playGame()