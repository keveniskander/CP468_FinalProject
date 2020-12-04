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
from colorama import Fore, Back, Style


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
        random_list=list(range(0,self.n))
        random.shuffle(random_list)

        for i in range (len(self.table)):
            random_row=random_list.pop()
            # random_row=random.randint(0,self.n-1)
            
            print("random item from list:")

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
            # print("Row: ", row)
            # print("Col: ", col)
            diag_conflicts = self.conflicts_diag(row, col)
            cardinal_conflicts = self.conflicts_cardinal(row, col)
            conflicts = diag_conflicts + cardinal_conflicts
            self.queens[i].conflicts = conflicts
            # print("Conflicts: ", conflicts)
        return

    def current_queen_conflicts(self,row,col):
        

        # print("Row: ", row)
        # print("Col: ", col)
        diag_conflicts = self.conflicts_diag(row, col)
        cardinal_conflicts = self.conflicts_cardinal(row, col)
        conflicts = diag_conflicts + cardinal_conflicts
        
        # print("Conflicts: ", conflicts)
        return conflicts
    

    def printBoard(self):
        for i in range(len(self.table)):
            for j in range (len(self.table)):
                print(self.table[i][j]," ",end="")
            print()
        return

    # #max_steps = number of steps allowed before giving up
    def min_conflicts(self, max_steps):
        max_steps=0

        while (self.is_solved()==False):

            list_queens=self.queens
            
            new_queen=random.randint(0,self.n-1)
            
            queen=list_queens[new_queen]
            

            moves=self.possible_moves(queen)

            min_conflicts= queen.conflicts
            min_pos= (queen.row,queen.col)
            # print("queen picked col=",queen.col)

            
            for move in moves:
                row=move[0]
                col=move[1]
                new_conflicts= self.current_queen_conflicts(row,col)

                if (new_conflicts<=min_conflicts):

                    min_conflicts=new_conflicts

                    min_pos= (row,col)

                # if (min_conflicts!=queen.conflicts):

            queen.conflicts=min_conflicts

            self.make_move(min_pos[0],min_pos[1],queen)

            
                
            # print()
            # print("new position:")
            # print("row:",min_pos[0])
            # print("col:",min_pos[1])
            # print("New Conflict:",queen.conflicts)
                # if (min_conflicts==0):
                #     print("added to solved")
                #     solved+=1
            max_steps+=1

        print('DONE')


        return

    # def update_queen_conflict(self,row,col,queen):

    #     queen.conflicts= self.current_queen_conflicts(row,col,queen)

    #     return

    def make_move(self,row,col,queen):
        
        if (row!=queen.row ):
            print("THIS SHOULD CHANGE TABLE")
            

            self.table[row][col]=1
            self.table[queen.row][queen.col]=0
            queen.row=row
            queen.col=col
            self.update_conflicts()
            self.printBoard()
        return

    def possible_moves(self,queen):
        
        col=queen.col
        moves=[]

        for i in range (self.n):
            if (i!=queen.row):

                moves.append((i,col))

        return moves

    def is_solved(self):
        is_solved=False

        conflicts_finished=0

        for i in range(len(self.queens)):
            if (self.queens[i].conflicts==0):
                conflicts_finished+=1

        if (conflicts_finished==self.n):
            is_solved=True



        return is_solved




  
   



    

def main():
    print("\033[1;37;40m Bright Colour\033[0;37;40m \n")

    board=Board(4)

    board.printBoard()

    board.update_conflicts()

    # print("POSSIBLE MOVES FOR QUEEN")
    # print(board.possible_moves(board.queens[0]))

    print("-----------------------------------------------------")
    print("MIN_CONFLICTS")

    board.min_conflicts(0)
    board.printBoard()

    print("Board is solved?: ",board.is_solved())
    
    


   



if __name__ == "__main__":
    main()

