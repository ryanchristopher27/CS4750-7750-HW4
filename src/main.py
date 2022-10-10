# Main File

from re import L

from board import GameBoard
from player import Player


def main():
    test()





def test():
    testBoard = GameBoard(5, 6)
    # player1 = Player(2, "Player 1", "x")
    testBoard.placeMove(0, 0, "x")


main()