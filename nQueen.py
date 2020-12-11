"""
-------------------------------------------------------
nQueen.py
Places N (int) queens on any given NxN chessboard so 
that no two queens are able to attack each other. 
-------------------------------------------------------
CP468
Final Project
Authors:  Keven Iskander, Carla Castaneda, Nicole Laslavic, Alexander Francis
__updated__ = "2020-11-24"
---------
"""
import random
import time

MAX_TABU=300


class Queen:
    value = 0
    row = 0
    col = 0
    def __init__(self, value, row, col):
        self.value = value #Value of all queens on board is 1, 0 on the board represents empty spaces.
        self.row = row
        self.col = col
        return

    def __int__(self):
        return int(self.value)


class Board:
    def __init__(self, n=None, queens=None):
        if queens is None:
            pass
        self.totalconflicts=0

        self.table = []
        self.n = n
        self.queens = []
        if n is not None:
            for _ in range(n):
                row = []
                for _ in range(n):
                    row.append(0)
                self.table.append(row)
            self.add_queens()
        return


    def add_queens(self):
        """
        -------------------------------------------------------
        Adds queens randomly to board. Queens are set in individual rows and columns.
        Parameters: self - Board
        Return: None
        -------------------------------------------------------
        """
        random_list = list(range(0, self.n))
        random.shuffle(random_list)
        for i in range(len(self.table)):
            random_row = random_list.pop()
            # random_row=random.randint(0,self.n-1)
            self.table[random_row][i] = 1
            self.queens.append(Queen(1, random_row, i))
        self.update_conflicts()
        return


    def conflicts(self, row, col):
        """
        -------------------------------------------------------
        Returns integer value representing number of other queens
        that diagonally conflict with the specified coordinates.
        Parameters: self - Board
                    row - row location
                    col - column location
        Return: value - number of conflicts
        -------------------------------------------------------
        """
        count = 0
        value1 = row+col
        value2 = row-col
        for i in range(self.n):
            opp_value1 = self.queens[i].row + self.queens[i].col
            opp_value2 = self.queens[i].row - self.queens[i].col
            if self.queens[i].row == row and self.queens[i].col == col:
                continue
            if row == col and self.queens[i].row == self.queens[i].col:
                count += 1
            if value1 == opp_value1 or value2 == opp_value2:
                count += 1
            if row == self.queens[i].row and col == self.queens[i].col:
                continue
            if row == self.queens[i].row or col == self.queens[i].col:
                count + 1
        return count


    def update_conflicts(self):
        """
        -------------------------------------------------------
        Sets totalconflicts to 1 if there is at least 1 conflict.
        Will return 0 if the board is solved and has no conflicts.
        Parameters: self - Board
        Return: None
        -------------------------------------------------------
        """
        self.totalconflicts=0
        for i in range(len(self.queens)):
            row = self.queens[i].row
            col = self.queens[i].col
            conflicts = self.conflicts(row, col)
            # self.queens[i].conflicts = conflicts
            if conflicts > 0:
                self.totalconflicts = 1
                return
        return


    def print_board(self):
        """
        -------------------------------------------------------
        Prints board
        Parameters: self - Board
        Return: None
        -------------------------------------------------------
        """
        for i in range(len(self.table)):
            for j in range(len(self.table)):
                print(self.table[i][j], " ", end="")
            print()
        return


    def solver(self):
        """
        -------------------------------------------------------
        This solver uses min_conflicts with tabu search to solve the queens problem.
        Parameters: self - Board
        Return: None
        -------------------------------------------------------
        """
        tabu = [[0 for i in range(len(self.table))] for j in range(len(self.table))]
        x = 0
        while self.totalconflicts > 0:
            new_queen = random.randint(0, len(self.queens) - 1)
            row = self.queens[new_queen].row
            col = self.queens[new_queen].col
            if self.conflicts(row, col)>0:
                moves = self.possible_moves(self.queens[new_queen])
                not_tabu = []

                for i in range(len(moves)):
                    if tabu[moves[i][0]][moves[i][1]] <= x:
                        not_tabu.append(moves[i])

                if len(not_tabu)>0:
                    min_move = not_tabu[0]
                    min_conflict = self.conflicts(not_tabu[0][0], not_tabu[0][1])
                    for k in range(len(not_tabu)):
                        current_conflict = self.conflicts(not_tabu[k][0], not_tabu[k][1])
                        if min_conflict >= current_conflict:
                            min_move = not_tabu[k]
                            min_conflict = current_conflict

                    tabu[self.queens[new_queen].row][self.queens[new_queen].col] = x + ((self.n)+10)

                    row=self.queens[new_queen].row
                    col=self.queens[new_queen].col

                    self.table[row][col]=0
                    self.table[min_move[0]][col]=1

                    # self.queens[new_queen].conflicts = min_conflict
                    self.queens[new_queen].row = min_move[0]
                    self.update_conflicts()
                    # self.is_solved()
                x+=1

        if (x==MAX_TABU):
            print("LIMIT")
        return  


    def possible_moves(self, queen):
        """
        -------------------------------------------------------
        Returns list of possible moves
        Parameters: self - Board
                    queen - selected queen piece
        Return: list - of possible moves the selected queen can make
        -------------------------------------------------------
        """
        col = queen.col
        moves = []
        for i in range(self.n):
            moves.append((i, col))
        return moves


    def is_solved (self):
        """
        -------------------------------------------------------
        Returns boolean value on solved status of board.
        Parameters: self - Board
        Return: valid - boolean value
        -------------------------------------------------------
        """
        valid = True
        self.update_conflicts()
        if self.totalconflicts > 0:
            valid = False
        return valid


def main():
    board = Board(300)
    start_time = time.time()
    board.print_board()
    board.solver()
    print("-------------")
    board.print_board()
    print("Board is solved?: ", board.is_solved())
    end_time = time.time()-start_time
    print()
    print("Execution Time: {:.3f} seconds".format(end_time))


if __name__ == "__main__":
    main()
