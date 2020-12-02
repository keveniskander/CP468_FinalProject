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

class Node:
    domain = 0
    value = 0
    def __init__(self, value, domain = domain,row=0,col=0):
        self.value = value
        self.domain = domain
        self.row=row
        self.col=col
        return

    def __int__(self):
        return int(self.value)

class Board:
    def __init__(self,n=None, queenLocations=[]):
        self.table = []
        self.n=n
        self.queenLocations = []
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
            location = (i, random_row)
            self.queenLocations.append(location)
        return

    def printBoard(self):

        for i in range(len(self.table)):
            for j in range (len(self.table)):
                print(self.table[i][j]," ",end="")

            print()

        return

    def min_conflicts(self):

        return


    def diagonalCheck(self, row, col):
        if(self.table[row][col] == 1):
            check = True
            a = row
            b = col
            #check bottom left
            while (check == True and a < self.n and b >= 0):
                a += 1
                b -= 1
                if (a >= self.n or b < 0):
                    break
                if (self.table[a][b] == 1):
                    check = False
            
            a = row
            b = col
            #check bottom right
            while (check == True and a < self.n and b < self.n):
                a += 1
                b += 1
                if (a >= self.n or b >= self.n):
                    break
                if (self.table[a][b] == 1):
                    check = False

            a = row
            b = col
            #check top right
            while (check == True and a >= 0 and b < self.n):
                a -= 1
                b += 1
                if (a < 0 or b >= self.n):
                    break
                if (self.table[a][b] == 1):
                    check = False

            a = row
            b = col
            #check top left
            while (check == True and a >= 0 and b >= 0):
                a -= 1
                b -= 1
                if (a < 0 or b < 0):
                    break
                if (self.table[a][b] == 1):
                    check = False

        return check

    def cardinalCheck(self, row, col):
        if(self.table[row][col] == 1):
            check = True
            a = row
            b = col
            #check above
            while (check == True and a < 0):
                a -= 1
                if (a < 0):
                    break
                if (self.table[a][b] == 1):
                    check = False
            
            a = row
            b = col
            #check bellow
            while (check == True and a < self.n):
                a += 1
                if (a >= self.n):
                    break
                if (self.table[a][b] == 1):
                    check = False

            a = row
            b = col
            #check right
            while (check == True and b < self.n):
                b += 1
                if (b >= self.n):
                    break
                if (self.table[a][b] == 1):
                    check = False

            a = row
            b = col
            #check left
            while (check == True and b >= 0):
                b -= 1
                if (b < 0):
                    break
                if (self.table[a][b] == 1):
                    check = False
        return check


    # returns number of conflicts
    def is_solved(self):
        result = True

        for i in range(self.n):
            for j in range(self.n):
                if self.table[i][j] == 1:
                    result1 = self.diagonalCheck(i,j)
                    result2 = self.cardinalCheck(i,j)
                    if result1 == False or result2 == False:
                        return False

        return result


def main():
    board=Board(7)
    board.printBoard()
    print(board.is_solved())


if __name__ == "__main__":
    main()
