import time
class Ground:
    def __init__(self,dist_fm_top=27):
        self.__y_coord = dist_fm_top
        self.__token = '-'

    def create_ground(self,board):
        dim = board.get_dims()
        # print(dim)        
        # time.sleep(2)
        # self._board.Place(0,dims[1],27,28,'-')
        board.Place(0,dim[1]-1,self.__y_coord,self.__y_coord,self.__token)