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

class Board:
    def __init__(self,n=None):
        self.table = []
        self.n=n
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

        return

    def printBoard(self):

        for i in range(len(self.table)):
            for j in range (len(self.table)):
                print(self.table[i][j]," ",end="")

            print()

        return

    def min_conflicts(self):

        return




        

def main():
    board=Board(7)

    board.printBoard()




    

if __name__ == "__main__":
    main()
