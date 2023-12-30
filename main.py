from random import choice


class TicTacToe:
    """
    Class to store the table, update it for each move and check the winner.

    Attributes:

    - table --> Array of 3 arrays of 3 single character elements
    - winner --> Blank if game is in progress, otherwise X, O, or draw
    Methods:

    - print --> ASCII print the table
    - update --> Updates the table with the player's move
    - win_check --> Check if there's a winner or draw
    """

    def __init__(self):
        self.table = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        self.line_array = ["a", "b", "c"]
        self.player = choice(["X", "O"])
        self.winner = ""

    def print(self):
        """
        ASCII print the table
        :return: nothing
        """
        print("    1   2   3  ")
        print("  -------------")
        for i in range(3):
            row = f"{self.line_array[i]} | "
            for j in range(3):
                row += self.table[i][j] + " | "
            print(row)
            print("  -------------")

    def update(self, pos) -> bool:
        """
        Updates the table
        :param pos: Coordinate in a1 format: a - line, 1 - column
        :return: True if move is possible
        """
        i = self.line_array.index(pos[0].lower())
        j = int(pos[1]) - 1
        if self.table[i][j] == " ":
            self.table[i][j] = self.player
            self.win_check()
            return True
        else:
            return False

    def win_check(self):
        """
        Check if there is a winner or the table is full and updates winner accordingly
        :return: nothing
        """
        # row check
        for i in range(3):
            if self.table[i][0] == self.table[i][1] == self.table[i][2] and self.table[i][0] != " ":
                self.winner = self.table[i][0]
        # column check
        for j in range(3):
            if self.table[0][j] == self.table[1][j] == self.table[2][j] and self.table[0][j] != " ":
                self.winner = self.table[0][j]
        # diagonal check
        if self.table[0][0] == self.table[1][1] == self.table[2][2] and self.table[0][0] != " ":
            self.winner = self.table[0][0]
        if self.table[2][0] == self.table[1][1] == self.table[0][2] and self.table[2][0] != " ":
            self.winner = self.table[2][0]
        # is full check
        empty_slots = False
        for i in range(3):
            for j in range(3):
                if self.table[i][j] == " ":
                    empty_slots = True
        if not empty_slots and self.winner == "":
            self.winner = "draw"

    def next_player(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"


ttt = TicTacToe()
ttt.print()
while ttt.winner == "":
    next_move = "  "
    # wait for player's input until a valid choice
    while len(next_move) != 2 \
            or next_move[0].lower() not in "abc" \
            or next_move[1] not in "123":
        next_move = input(f"Player {ttt.player}, your move (a1..c3): ")
    if ttt.update(next_move):
        # move successful, change player
        ttt.next_player()
        ttt.print()
    else:
        print("Incorrect move, try again!")

if ttt.winner == "draw":
    print("Play again, this was a draw!")
else:
    print(f"Congratulation player {ttt.winner}, you won!")
