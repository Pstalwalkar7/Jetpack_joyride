from person import Person 
import time
class Bullet(Person):
    def __init__(self,x_coord,y_coord,dir):
        lives=1
        Person.__init__(self,x_coord,y_coord,1,1,True,dir,lives)
        self._shape1 = ['>']
        self._shape2 = ['<']
        self._allowed_collision+=[' ','$','P'] 
    
    def __del__(self):
        pass
    
    def Update_bullet(self,grid,copy,COL,pos_x):
        if self._x_coord < pos_x or self._x_coord > pos_x + 204 or self._x_coord > COL -10 or self._lives<1 or self._x_coord < 10:
            self.disappear(grid,copy)
            # print("Destroyed:",self._lives)
            # time.sleep(1)
            del self
            return True
        else:
            self.disappear(grid,copy)
            for i in range(3):
                self._x_coord += self._direction
                self.check_collision(grid)
                if (self._direction>0 and self._allowed_right==False) or (self._direction<0 and self._allowed_left==False):
                    self._lives -= 1
                    return self._x_coord,self._y_coord
                
            self.position(grid,copy)
            return