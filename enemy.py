from person import Person
import time
from colorama import Fore as fg
from colorama import Back as bg
class Enemy(Person):
    def __init__(self,x_coord,y_coord):
        size_x = 39
        size_y = 15
        Person.__init__(self,x_coord,y_coord,size_x,size_y,True,0,10)
        self._shape1.append([' ','<','>','=','=','=','=','=','=','=','(',')']+[' ' for j in range(27)])
        self._shape1.append(['(','/','\\','_','_','_',' ',' ',' ','/','|','\\','\\']+[' ' for i in range(10)]+['(',')'] + ['=' for i in range(10)]+ ['<','>','_',' '])
        self._shape1.append([' ' for k in range(6)]+['\\','_','/',' ','|',' ','\\','\\']+[' ' for i in range(8)]+['/','/','|','\\',' ',' ',' ']+['_' for i in range(6)]+['/',' ','\\',')'])
        self._shape1.append([' ' for i in range(8)]+ ['\\','_','|',' ',' ','\\','\\']+[' 'for i in range(6)]+['/','/',' ','|',' ','\\','_','/']+[' ' for i in range(10)])
        self._shape1.append([' ' for i in range(10)]+['\\','|','\\','/','|','\\','_',' ',' ',' ','/','/',' ',' ','/','\\','/']+[' ' for i in range(12)])
        self._shape1.append([' ' for i in range(11)]+['(','o','o',')','\\',' ','\\','_','/','/',' ',' ','/']+[' ' for i in range(15)])
        self._shape1.append([' ' for i in range(10)]+['/','/','_','/','\\','_','\\','/',' ','/',' ',' ','|']+[' ' for i in range(16)])
        self._shape1.append([' ' for i in range(9)]+['@','@','/',' ',' ','|','=','\\',' ',' ','\\',' ',' ','|']+[' ' for i in range(16)])
        self._shape1.append([' ' for i in range(14)] + ['\\','_','=','\\','_',' ','\\',' ','|'] + [' ' for i in range(16)])
        self._shape1.append([' ' for i in range(16)] + ['\\','=','=','\\',' ','\\','|','\\','_'] + [' ' for i in range(14)])
        self._shape1.append([' ' for i in range(13)] + ['_','_','(','\\','=','=','=','\\','(',' ',' ',')','\\'] +[' ' for i in range(13)])
        self._shape1.append([' ' for i in range(12)] + ['(','(','(','~',')',' ','_','_','(','_','/',' ',' ','|'] + [' ' for i in range(13)])
        self._shape1.append([' ' for i in range(15)] + ['(','(','(','~',')',' ','\\',' ',' ','/'] + [' ' for i in range(14)])
        self._shape1.append([' ' for i in range(15)] + ['_' for i in range(6)] + ['/',' ','/'] + [' ' for i in range(15)])
        self._shape1.append([' ' for i in range(15)] + ["'",'-','-','-','-','-','-',"'"] + [' ' for i in range(16)])    
        self._not_damage=['|','O','|','\\','/','^']
        self._shape2+=self._shape1

    def __del__(self):
        pass

    def fight(self,hero,MAT,COPY):
        flag = True
        dims = hero.get_dim()
        coords = hero.get_coords()
        self.position(MAT,COPY)
        while self._lives>0 and coords[1] + dims[1] - 1 < 7 and coords[1] + dims[1] -1 < self._y_coord and self._y_coord>0 :
            self.disappear(MAT,COPY)
            self._y_coord -=1
            self.position(MAT,COPY)

        while self._lives>0 and coords[1] > 19 and self._y_coord + 15 - 1 < coords[1]:
            self.disappear(MAT,COPY)
            self._y_coord +=1
            self.position(MAT,COPY)

        while  self._lives >0 and coords[1] >= 7 and coords[1] <= 19:
            if self._y_coord + 7 > coords[1] :      # hero head is below dragon mouth
                self.disappear(MAT,COPY)
                self._y_coord -= 1
                self.position(MAT,COPY)

            elif self._y_coord + 7 < coords[1] :
                self.disappear(MAT,COPY)
                self._y_coord +=1
                self.position(MAT,COPY)
            
            else:
                break
