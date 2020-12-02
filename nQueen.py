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

class Queen:
    value = 0
    conflicts = 0
    row = 0
    col = 0
    def __init__(self, value, conflicts, row, col):
        self.value = value
        self.conflicts = conflicts
        self.row=row
        self.col=col
        return

    def __int__(self):
        return int(self.value)

class Board:
    def __init__(self, n=None, queens=[]):
        self.table = []
        self.n=n
        self.queens = []
        if n!=None:

            for _ in range (n):
                row=[]
                for _ in range(n):
                    row.append(0)

                self.table.append(row)
            self.add_queens()

        return

    def add_queens(self):

        for i in range (len(self.table)):
            random_row=random.randint(0,self.n-1)

            self.table[random_row][i]=1
        
            self.queens.append(Queen(1, 0, random_row, i))
        
        self.update_conflicts()
        return

    def conflicts_diag(self, row, col):
        value = 0
        a = row
        b = col
        
        #check bottom left
        while (a < self.n and b >= 0):
            a += 1
            b -= 1
            if (a >= self.n or b < 0):
                break
            if (self.table[a][b] == 1):
                value += 1
        
        a = row
        b = col
        #check bottom right
        while (a < self.n and b < self.n):
            a += 1
            b += 1
            if (a >= self.n or b >= self.n):
                break
            if (self.table[a][b] == 1):
                value += 1

        a = row
        b = col
        #check top right
        while (a >= 0 and b < self.n):
            a -= 1
            b += 1
            if (a < 0 or b >= self.n):
                break
            if (self.table[a][b] == 1):
                value += 1

        a = row
        b = col
        #check top left
        while (a >= 0 and b >= 0):
            a -= 1
            b -= 1
            if (a < 0 or b < 0):
                break
            if (self.table[a][b] == 1):
                value += 1

        return value
    
    def conflicts_cardinal(self, row, col):
        value = 0
        a = row
        b = col
        #check above
        while (a < 0):
            a -= 1
            if (a < 0):
                break
            if (self.table[a][b] == 1):
                value += 1
        
        a = row
        b = col
        #check bellow
        while (a < self.n):
            a += 1
            if (a >= self.n):
                break
            if (self.table[a][b] == 1):
                value += 1

        a = row
        b = col
        #check right
        while (b < self.n):
            b += 1
            if (b >= self.n):
                break
            if (self.table[a][b] == 1):
                value += 1

        a = row
        b = col
        #check left
        while (b >= 0):
            b -= 1
            if (b < 0):
                break
            if (self.table[a][b] == 1):
                value += 1
        return value

    def update_conflicts(self):
        for i in range(len(self.queens)):
            row = self.queens[i].row
            col = self.queens[i].col
            print("Row: ", row)
            print("Col: ", col)
            diag_conflicts = self.conflicts_diag(row, col)
            cardinal_conflicts = self.conflicts_cardinal(row, col)
            conflicts = diag_conflicts + cardinal_conflicts
            self.queens[i].conflicts = conflicts
            print("Conflicts: ", conflicts)
        return

    def printBoard(self):
        for i in range(len(self.table)):
            for j in range (len(self.table)):
                print(self.table[i][j]," ",end="")
            print()
        return

    # #max_steps = number of steps allowed before giving up
    def min_conflicts(self, max_steps):


        return

  
   



    

def main():
    board=Board(8)

    board.printBoard()

    board.update_conflicts()

    print(board.is_solved())



if __name__ == "__main__":
    main()

