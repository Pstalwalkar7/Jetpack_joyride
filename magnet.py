from coins import Coins
class Magnet(Coins):
    def __init__(self,x_coord,y_coord):
        Coins.__init__(self,x_coord,y_coord)
        self._token = 'M'

    def create_obj(self,board):
        if board.check_empty(self._x_coord,self._x_coord,self._y_coord,self._y_coord) == True:
            board.Place(self._x_coord,self._x_coord,self._y_coord,self._y_coord,self._token)
            return True
        return False