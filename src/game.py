# game class

from board import GameBoard
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

    def __init__(self, p1MovesAhead, p2MovesAhead, boardRowSize, boardColSize):
        # generate board    
        gameboard = GameBoard(boardRowSize, boardColSize)
        
        # set player 1
        player1 = Player(p1MovesAhead, "Player 1", "X")

        # set player 2
        player2 = Player(p2MovesAhead, "Player 2", "O")


