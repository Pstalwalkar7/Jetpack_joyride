from person import Person
from colorama import Back as bg
from colorama import init
from colorama import Fore as fg
from colorama import Style
# init(autoreset =True)
class Mandalorian(Person):
    def __init__(self,x_coord,y_coord):
        size_x=3
        size_y=3
        lives=5
        dir=1
        Person.__init__(self,x_coord,y_coord,size_x,size_y,False,dir,lives)
        self._shape1 = [ ["|", 'O', "|"], [" ", "\\", " "], ["^", " ", "^"] ]
        self._copy1 = [ ["|", 'O', "|"], [" ", "\\", " "], ["^", " ", "^"] ]
        self._shape2 = [ ["|", "O", "|"], [" ", "/", " "], ["^", " ", "^"] ]
        self._copy2 = [ ["|", "O", "|"], [" ", "/", " "], ["^", " ", "^"] ]
        self._not_damage = ["$","-"," "]
        self._shield = True
        self._allowed_collision += [" ","$","P"]
        self._collectable+=["$",'P']
        self._death=False
        self._attracted=False
        for i in range(len(self._shape1)):
            for j in range(len(self._shape1[i])):
                if self._shield == True:
                    self._shape1[i][j] = fg.RED + self._shape1[i][j]

    def shielded(self):
        if self._shield == True:
            print(Style.RESET_ALL)
            for i in range(len(self._shape1)):
                for j in range(len(self._shape1[i])):
                    self._shape1[i][j] = bg.RED + self._copy1[i][j]
                    self._shape2[i][j] = bg.RED + self._copy2[i][j]
            print(Style.RESET_ALL)
        else:
            print(Style.RESET_ALL)
            # Fore.WHITE+Style.RESET_ALL
            # init(strip=False)

            # for i in self._shape1:
            #     for j in i:
            #         j = fg.WHITE + j
            
            # for i in self._shape2:
            #     for j in i:
            #         j = fg.WHITE + j
            
            for i in range(len(self._shape1)):
                for j in range(len(self._shape1[i])):
                    self._shape1[i][j] = bg.CYAN + fg.BLACK + self._copy1[i][j]
                    self._shape2[i][j] = bg.CYAN + fg.BLACK + self._copy2[i][j]
            print(Style.RESET_ALL)
            # self._shape1 =  fg.WHITE+[ ["|", 'O', "|"], [" ", "\\", " "], ["^", " ", "^"] ]
            # self._shape2  =  fg.WHITE+[ ["|", "O", "|"], [" ", "/", " "], ["^", " ", "^"] ]

    def get_not_damage(self):
        return self._not_damage

    def get_attracted(self):
        return self._attracted

    def set_attracted(self,value):
        self._attracted = value 

    def get_shield(self):
        return self._shield

    def set_shield(self,value):
        self._shield = value

    def fall(self,rate):
        self._y_coord+=rate
        # if self.y_coord + 3 > 40 :
        #     self.y_coord = 40 - 3

    def attract(self,x_mag,y_mag):
        if self._x_coord < x_mag and self._allowed_right==True:
            self._x_coord += 1
        elif self._x_coord > x_mag and self._allowed_left==True:
            self._x_coord -= 1

        if self._y_coord < y_mag and self._allowed_down==True:
            self._y_coord +=1
        elif self._y_coord > y_mag and self._allowed_up==True:
            self._attracted=True    # disables gravity
            self._y_coord -=1

        