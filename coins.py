import random
# from board import Board
class Coins:
    def __init__(self,x_coord,y_coord):
        self._token = '$'
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_coords(self):
        return self._x_coord,self._y_coord

    def set_coords(self,x,y):
        self._x_coord = x
        self._y_coord = y

    def create_obj(self,board):
        dims = board.get_dims()
        form = random.randint(1,2)
        start_x = self._x_coord
        start_y = self._y_coord
        end_x = start_x
        end_y = start_y
        if form == 1:
            end_x = start_x + 5
            if end_x >= dims[1]:
                end_x = dims[1] - 1
        else:
            end_y = start_y + 5
            if end_y >= 27:
                end_y = 27 - 1

        flag = board.check_empty(start_x,end_x,start_y,end_y)
        if flag == True:
            board.Place(start_x,end_x,start_y,end_y,self._token)
        return flag
