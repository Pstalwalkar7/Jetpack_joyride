#####################JUMPING, JUMPING DIR, POSITION METH????????????? ########################
import time
class Person:
    def __init__(self,x_coord,y_coord,size_x,size_y,is_moving,dir,lives):
        """ Initializes the position of the  character. Also, we initialize the size of character, and 2 shapes, the way it should look while going forward and the other 
        while going back. Also we determine the direction of moving, if any."""
        self._x_coord=x_coord
        self._y_coord=y_coord
        self._size_x=size_x
        self._size_y=size_y
        self._shape1=[]
        self._shape2=[]
        self._allowed_collision=[]      # All the items which can be passed -- can be erased and replaced by the character. for counterexample, Walls and other characters are not allowed
        # if character is moving (True) and direction is 0 then : uncertain / both , +1 : +x axis, -1: -x axis ; moving = False: Stationary 
        self._moving=is_moving
        self._falling=False
        self._direction=dir
        self._lives=lives
        self._collectable=[]
        self._allowed_up=True
        self._allowed_down=True
        self._allowed_right=True
        self._allowed_left=True

    def get_coords(self):
        return self._x_coord, self._y_coord

    def set_coords(self,x,y):
        self._x_coord = x
        self._y_coord = y

    def get_dim(self):
        return self._size_x , self._size_y

    def get_shapes(self):
        return self._shape1, self._shape2

    def get_allowed_collision(self):
        return self._allowed_collision

    def get_collectable(self):
        return self._collectable

    def get_moving(self):
        return self._moving

    def set_moving(self,val):
        self._moving = val

    def get_falling(self):
        return self._falling

    def set_falling(self,val):
        self._falling = val
    
    def get_direction(self):
        return self._direction

    def set_direction(self,value):
        self._direction = value

    def get_lives(self):
        return self._lives

    def set_lives(self,lives):
        self._lives = lives

    def get_allowed(self):
        return self._allowed_up, self._allowed_down, self._allowed_right, self._allowed_left

    def set_allowed(self,L):
        self._allowed_up = L[0]
        self._allowed_down = L[1]
        self._allowed_right = L[2]
        self._allowed_left = L[3]

    def die(self,grid):
        if self._lives <= 0:
            for i in range(self._size_y):
                for j in range(self._size_x):
                    grid[self._y_coord + i][self._x_coord + j]=' '
            del self
            return True
        return False

    def disappear(self,grid,orig):
        """Make the character vanish. As if it never existed at the point. Use with next method to work out motion"""
        for i in range(self._y_coord,self._y_coord+self._size_y):
            for j in range(self._x_coord,self._x_coord+self._size_x):
                if orig[i][j] in self._collectable:
                    orig[i][j]=' '
                grid[i][j]=orig[i][j]
                    

    def position(self,grid,orig):
        """Makes a character appear at a particular point. ALSO USEFUL FOR INITIALIZING THE POSITION OF THE CHARACTERS"""
        coins=0 
        powerup = False
        try:
            for i in range(self._size_y):
                for j in range(self._size_x):
                    now=grid[self._y_coord + i][self._x_coord + j] 
                    if now in self._collectable:
                        orig[i][j]=' '
                        if now =='$':
                            coins+=1
                        elif now =='P':
                            powerup = True
                    grid[self._y_coord + i][self._x_coord + j]= self._shape1[i][j] if self._direction>=0 else self._shape2[i][j]
        except Exception as e:
            print(e)    
        return coins,powerup
        
    def check_collision(self,grid):
        """Checks whether person makes collision with any other object in the game. """
        self._allowed_up=True
        self._allowed_down=True
        self._allowed_right=True
        self._allowed_left=True
        
        # ABOVE :
        try:    # index error
            for i in range(self._size_x):
                if grid[self._y_coord-1][self._x_coord+i] not in self._allowed_collision:
                    self._allowed_up=False
                    break
        except:
            pass

        # BELOW:
        try:
            for i in range(self._size_y):
                if grid[self._y_coord+self._size_y][self._x_coord+i] not in self._allowed_collision:
                    self._allowed_down=False
                    break

        except:
            pass

        # LEFT
        try:
            for i in range(self._size_y):
                if grid[self._y_coord+i][self._x_coord-1] not in self._allowed_collision:
                    self._allowed_left=False
                    break
        except:
            pass

        # RIGHT
        try:
            for i in range(self._size_y):
                if grid[self._y_coord+i][self._x_coord+self._size_x] not in self._allowed_collision:
                    self._allowed_right=False
                    break
        except:
            pass