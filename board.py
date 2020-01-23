import random
import time
from colorama import Back as bg
from colorama import Fore as fg

class Board:
    def __init__(self,rows,columns,speed=1):
        """Initializes the board's rows and columns and matrix to an empty matrix"""
        ######SPEED!!
        self.__rows=rows
        self.__columns=columns
        self.__matrix=[[" " for j in range(columns)]for i in range(rows)]
        self.__copy=[[" " for i in range(columns)]for j in range(rows)]
        self.__speed=speed
    
    def get_dims(self):
        return self.__rows,self.__columns

    def get_matrix(self):
        return self.__matrix

    def set_matrix(self,MAT):
        self.__matrix = MAT

    def get_copy(self):
        return self.__copy

    def set_copy(self,MAT):
        self.__copy = MAT

    def Place(self,start_x,end_x,start_y,end_y,token):
        # print("1")
        # time.sleep(2)
        for i in range(start_y,end_y+1):
            for j in range(start_x,end_x+1):
                self.__matrix[i][j] = token
        
        # for i in range(start_y,end_y):
        #     for j in range(start_x,end_x):
        #         print(self.__matrix[i][j])
        

    def PlaceCopy(self,start_x,end_x,start_y,end_y,token):
        for i in range(start_y,end_y):
            for j in range(start_x,end_x):
                self.__copy[i][j] = token

    def get_speed(self):
        return self.__speed

    def set_speed(self,speed):
        self.__speed = speed

    def CopyBoard(self):
        for i in range(self.__rows):
            for j in range(self.__columns):
                self.__copy[i][j]=self.__matrix[i][j]

    def PrintBoard(self,starting_col,at_a_time=204):
        ending_col=starting_col+at_a_time
        if(ending_col>self.__columns):
            ending_col=self.__columns-1
        for i in range(self.__rows):
            for j in range(starting_col,ending_col):
                if self.__matrix[i][j]=='$':
                    print (bg.GREEN + self.__matrix[i][j],end='')
                elif self.__matrix[i][j]=='*':
                    print (bg.YELLOW + self.__matrix[i][j],end='')
                elif self.__matrix[i][j]==' ' or self.__matrix[i][j]=='-':
                    print(bg.CYAN + self.__matrix[i][j],end='')
                else:
                    print(bg.CYAN + self.__matrix[i][j],end='')
            print()
        return ending_col==self.__columns-1

    def check_empty(self,start_x,end_x,start_y,end_y):
        if start_x == end_x:
            for i in range(start_y,end_y+1):
                if self.__matrix[i][start_x] != ' ':
                    return False
            return True
        elif start_y == end_y:
            for i in range(start_x,end_x+1):
                if self.__matrix[start_y][i] != ' ':
                    return False
            return True
        else:
            print("CHECK_EMPTY CONSTRAINTS UNFOLLOWED")
            sleep(10)

    def a8_h1_empty(self,start_x,start_y,minidiff):
        for i in range(minidiff):
            if self.__matrix[start_y+i][start_x+i] != ' ':
                return False
        return True

    def a8_h1_fill(self,start_x,start_y,minidiff,token):
        for i in range(minidiff):
            self.__matrix[start_y + i][start_x + i] = token
    
    def h8_a1_empty(self,start_x,start_y,minidiff):
        for i in range(minidiff):
            if self.__matrix[start_y+i][start_x-i]!=' ':
                return False
        return True

    def h8_a1_fill(self,start_x,start_y,minidiff,token):
        for i in range(minidiff):
            self.__matrix[start_y+i][start_x-i] = token