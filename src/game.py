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

    def __init__(self, p1MovesAhead, p2MovesAhead, boardRowSize, boardColSize):
        # generate board    
        self.gameboard = GameBoard(boardRowSize, boardColSize)
        
        # set player 1
        self.player1 = Player(p1MovesAhead, "Player 1", 1)

        # set player 2
        self.player2 = Player(p2MovesAhead, "Player 2", -1)
            

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

    def printBoard(self):
        print("--- Current Game Board ---")
        for row in self.gameboard.board:
            print(row)



    #logic functions 

    def playGame(self):
        print("Starting Game")
        while(self.gameboard.terminal == False):
            # may have to check after each player moves if terminal is true. 
            self.addMoveSequence(minimaxSearch(self.getGameBoard(), self.player1.playerSymbol, self.player1.movesAhead))
            self.addMoveSequence(minimaxSearch(self.getGameBoard(), self.player2.playerSymbol, self.player2.movesAhead))
            #print(self.moveSequence)

        if(self.gameboard.winner == -1):
            print("Player 1 won the game")
        
        elif(self.gameboard.winner == 1):
            print("player 2 won the game")
        
        elif(self.gameboard.winner == 0):
            print("There was a tie")
        
        else:
            print("Something went wrong")

game1 = Game(0,0, 5, 4)
print("Hello")
game1.printBoard()
game1.gameboard.placeMove(1, 2, "x")
game1.printBoard()
game1.gameboard.placeMove(2, 1, "o")
game1.printBoard()
# game1.playGame()