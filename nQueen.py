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
    conflicts = 0
    row = 0
    col = 0

    def __init__(self, value, conflicts, row, col):
        self.value = value
        self.conflicts = conflicts
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
        Adds queens randomly to board.
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
            self.queens.append(Queen(1, 0, random_row, i))
        self.update_conflicts()
        return

    def conflicts_diag(self, row, col):
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
        value = 0
        a = row
        b = col
        # check bottom left
        while a < self.n and b >= 0:
            a += 1
            b -= 1
            if a >= self.n or b < 0:
                break
            if self.table[a][b] == 1:
                value += 1
        a = row
        b = col
        # check bottom right
        while a < self.n and b < self.n:
            a += 1
            b += 1
            if a >= self.n or b >= self.n:
                break
            if self.table[a][b] == 1:
                value += 1
        a = row
        b = col
        # check top right
        while a >= 0 and b < self.n:
            a -= 1
            b += 1
            if a < 0 or b >= self.n:
                break
            if self.table[a][b] == 1:
                value += 1
        a = row
        b = col
        # check top left
        while a >= 0 and b >= 0:
            a -= 1
            b -= 1
            if a < 0 or b < 0:
                break
            if self.table[a][b] == 1:
                value += 1
        
        
        return value

    def conflicts_cardinal(self, row, col):
        """
        -------------------------------------------------------
        Returns integer value representing number of other queens
        that are directly above, below, to the left and right of the location specified.
        Parameters: self - Board
                    row - row location
                    col - column location
        Return: value - number of conflicts
        -------------------------------------------------------
        """
        value = 0
        a = row
        b = col
        # check above
        while a < 0:
            a -= 1
            if a < 0:
                break
            if self.table[a][b] == 1   :
                value += 1
        a = row
        b = col
        # check bellow
        while a < self.n:
            a += 1
            if a >= self.n:
                break
            if self.table[a][b] == 1 :
                value += 1
        a = row
        b = col
        # check right
        while b < self.n:
            b += 1
            if b >= self.n:
                break
            if self.table[a][b] == 1 :
                value += 1
        a = row
        b = col
        # check left
        while b >= 0:
            b -= 1
            if b < 0:
                break
            if self.table[a][b] == 1 :
                value += 1
        
        

        return value

    def update_conflicts(self):
        """
        -------------------------------------------------------
        Updates conflicts of all queens.
        Parameters: self - Board
        Return: None
        -------------------------------------------------------
        """
        self.totalconflicts=0
        for i in range(len(self.queens)):
            row = self.queens[i].row
            col = self.queens[i].col
            diag_conflicts = self.conflicts_diag(row, col)
            cardinal_conflicts = self.conflicts_cardinal(row, col)
            conflicts = diag_conflicts + cardinal_conflicts
            self.queens[i].conflicts = conflicts
            # print("self.queens",self.queens[i].row, self.queens[1].col)
            # print("self.queens conflicts",self.queens[i].conflicts)

            self.totalconflicts+=conflicts
        return

    def current_queen_conflicts(self, row, col):
        """
        -------------------------------------------------------
        Returns number of conflicts if a queen were to move into a certain spot.
        Does not change the conflicts value.
        Parameters: self - Board
                    row - row of queens location
                    col - column of queens location
        Return: conflicts - number of conflicts if queen were to 
                            move into specified row and col
        -------------------------------------------------------
        """
        diag_conflicts = self.conflicts_diag(row, col)
        cardinal_conflicts = self.conflicts_cardinal(row, col)
        conflicts = diag_conflicts + cardinal_conflicts
        return conflicts

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

    # #max_steps = number of steps allowed before giving up
    def min_conflicts(self):
        """
        -------------------------------------------------------
        Solves queen problem
        Parameters: self - Board
                    max_steps - Maximum number of steps allowed to make
        Return: None
        -------------------------------------------------------
        """
        max_steps = 0
        print("self.conflicts:",self.totalconflicts)
        while self.totalconflicts!=0 and max_steps < 500:
            list_queens = self.queens
            new_queen = random.randint(0, self.n - 1)
            queen = list_queens[new_queen]
            moves = self.possible_moves(queen)
            min_conflicts = queen.conflicts
            min_pos = (queen.row, queen.col)
            # print("queen picked col=",queen.col)
            for move in moves:
                row = move[0]
                col = move[1]
                new_conflicts = self.current_queen_conflicts(row, col)
                if new_conflicts <= min_conflicts:
                    min_conflicts = new_conflicts
                    min_pos = (row, col)
                # if (min_conflicts!=queen.conflicts):
            queen.conflicts = min_conflicts
            self.make_move(min_pos[0], min_pos[1], queen)
            # print()
            # print("new position:")
            # print("row:",min_pos[0])
            # print("col:",min_pos[1])
            # print("New Conflict:",queen.conflicts)
            # if (min_conflicts==0):
            #     print("added to solved")
            #     solved+=1
            max_steps += 1
        print('DONE')
        return

    def tabu_search(self):
            
            tabu = [[0 for i in range(len(self.table))] for j in range(len(self.table))]
            
            x = 0
            
            while self.totalconflicts>0 :
                new_queen = random.randint(0, len(self.queens) - 1)
                if self.queens[new_queen].conflicts>0:
                    moves = self.possible_moves(self.queens[new_queen])
                    not_tabu = []

                    # print("--------------")
                    # print("queen",self.queens[new_queen].row,self.queens[new_queen].col)
                    
                    for i in range(len(moves)):
                        if tabu[moves[i][0]][moves[i][1]] <= x:
                            not_tabu.append(moves[i])

                    if len(not_tabu)>0:
                        min_move = not_tabu[0]
                        min_conflict = self.current_queen_conflicts(not_tabu[0][0], not_tabu[0][1])
                        for k in range(len(not_tabu)):
                            current_conflict = self.current_queen_conflicts(not_tabu[k][0], not_tabu[k][1])
                            if min_conflict >= current_conflict:
                                min_move = not_tabu[k]
                                min_conflict = current_conflict

                        tabu[self.queens[new_queen].row][self.queens[new_queen].col] = x + ((self.n)+10)

                        row=self.queens[new_queen].row
                        col=self.queens[new_queen].col

                        self.table[row][col]=0
                        self.table[min_move[0]][col]=1
                        # print("not tabu",not_tabu)
                        # print("moves",moves)
                        # print("min move:",min_move)
                        # self.print_board()

                        self.queens[new_queen].conflicts = min_conflict
                        self.queens[new_queen].row = min_move[0]
                        self.update_conflicts()
                #print(x)
        
                    
                    x+=1
            # print(x)
            # print(self.totalconflicts)
            if (x==MAX_TABU):
                print("LIMIT")

            
            return  

    def make_move(self, row, col, queen):
        """
        -------------------------------------------------------
        Makes specified queen move to new location. 
        Parameters: self - Board
                    row - row location
                    col - column location
                    queen - queen piece
        Return: None
        -------------------------------------------------------
        """
        if row != queen.row:
            # print("THIS SHOULD CHANGE TABLE")
            self.table[row][col] = 1
            self.table[queen.row][queen.col] = 0
            queen.row = row
            queen.col = col
            self.update_conflicts()
            # self.printBoard()
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

    def is_solved(self):
        """
        -------------------------------------------------------
        Returns boolean value of solved status of Board 
        Parameters: self - Board
        Return: Boolean - True if board is solved
                          False if board is not solved
        -------------------------------------------------------
        """
        is_solved = False
        conflicts_finished = 0
        for i in range(len(self.queens)):
            if self.queens[i].conflicts == 0:
                conflicts_finished += 1
        if conflicts_finished == self.n:
            is_solved = True
        return is_solved


def main():
    board = Board(100)
    start_time = time.time()
    # board.print_board()
    
    # board.print_board()
    # board.update_conflicts()
    # # print("POSSIBLE MOVES FOR QUEEN")
    # # print(board.possible_moves(board.queens[0]))
    # print("-" * 30)
    # print("MIN_CONFLICTS")
    # board.min_conflicts()
    # board.print_board()
    # print("Board is solved?: ", board.is_solved())
    # end_time = time.time()-start_time
    # print()
    # print("Execution Time: {:.3f} seconds".format(end_time))
    board.tabu_search()
    # print("-------------")
    # board.print_board()
    print("Board is solved?: ", board.is_solved())


if __name__ == "__main__":
    main()
