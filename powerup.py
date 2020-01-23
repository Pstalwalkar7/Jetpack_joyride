from magnet import Magnet
class Powerup(Magnet):
    def __init__(self,x,y):
        Magnet.__init__(self,x,y)
        self._token = 'P'
    
    def create_obj(self,board):
        if board.check_empty(self._x_coord,self._x_coord,self._y_coord,self._y_coord) == True:
            board.Place(self._x_coord,self._x_coord,self._y_coord,self._y_coord,self._token)
            return True
        return False