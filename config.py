import os
import time
import random
import signal 
import getInput
from board import Board
from bullet import Bullet
from snowball import Snowball
from magnet import Magnet
from coins import Coins
from ground import Ground
from mandalorian import Mandalorian
from enemy import Enemy
from person import Person
from zapper import Zapper
from powerup import Powerup
from colorama import Fore as fg
from colorama import Back as bg

class Engine(Board,Mandalorian,Enemy,Bullet,Magnet,Coins,Ground,Zapper,Snowball):

    def __init__(self,rows = 30, cols = 1000, start_x = 23, start_y =17, boss_x =950, boss_y =5):
        self._score = 0
        self._coins =0
        self._board = Board(rows,cols)
        self._hero = Mandalorian(start_x,start_y)
        self._boss = Enemy(boss_x,boss_y)
        self._getch = getInput._getChUnix()
        self._rem_time = 100
        self._fired_bullets = []
        self._thrown_snowballs = []
        self._coins_placed = []
        self._zappers = []
        self._speedup = False
        self._magnet = Magnet(0,0)
        self._powerup = Powerup(0,0)
        self._speedup = False
        self._ground = Ground()

    def create_powerup(self):
        flag = False
        while flag == False:
            x=random.randint(100,700)
            y=random.randint(2,17)
            self._powerup.set_coords(x,y)
            flag = self._powerup.create_obj(self._board)

    def create_magnet(self):
        flag = False
        while flag == False:
            x=random.randint(100,700)
            y=random.randint(2,17)
            self._magnet.set_coords(x,y)
            flag = self._magnet.create_obj(self._board)

    def create_all_zappers(self):
        for i in range(1,20):  # 25 zappers
            mod=random.randint(5,34)
            start_x=mod + i*40
            start_y=random.randint(5,17)
            Z = Zapper(start_x,start_y)
            if Z.create_zapper(self._board) == True:
                self._zappers.append(Z)

    def create_all_coins(self):
        for i in range(9):
            mod  = random.randint(0,9)
            start_x= mod + i*85
            start_y = random.randint(5,17)
            C = Coins(start_x,start_y)
            if C.create_obj(self._board) == True:
                self._coins_placed.append(C)

    def run(self):
        pos_x = 0
        gravity = 1
        fall_at_time = 0
        mag_exists = True
        iterator = 0
        start = False
        dims = self._board.get_dims()
        MAT = self._board.get_matrix()
        COPY = self._board.get_copy()
        hero_size = self._hero.get_dim()
        not_damage = self._hero.get_not_damage()

        def alarmhandler(signum,frame):
            raise TypeError

        def getinp(timeout=0.15):
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                ch = self._getch()
                signal.alarm(0)
                return ch
            except TypeError:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''

        def terminate(msg):
            # os.system("killall -9 aplay")
            ##################UPDATE SCORE!! #########################
            os.system('reset')
            print(msg)
            exit()

        # self._board.Place(0,dims[1],0,dims[0],'*')
        self.create_all_coins()
        self.create_all_zappers()
        self.create_magnet()
        self.create_powerup()
        self._ground.create_ground(self._board)
        T = self._magnet.get_coords()
        x_mag = T[0]
        y_mag = T[1]
        print('\033[0;0H',end='')
        self._board.CopyBoard()
        # print(type(self._coins))
        X=self._hero.position(MAT,COPY)
        self._coins += X[0]
        self._speedup = self._speedup  or X[1]
        Z = Zapper(0,0)
        MAT = self._board.get_matrix()
        COPY = self._board.get_copy()
        self._boss.position(MAT,COPY)
        MAT = self._board.get_matrix()
        COPY = self._board.get_copy()
        self._hero.check_collision(MAT)
        T1 = time.time()
        T2 = T1
        T3 = T1
        last_activated = None
        start =True
        sped =False
        while True:
            # os.system('clear')
            self._score = self._coins * 50  + (10 - self._boss.get_lives()) * 1000
            # print(self._speedup)
            if (self._speedup == True and sped ==False):
                self._board.set_speed(self._board.get_speed()+1)
                sped =True
            if start == False and self._hero.get_shield() == True and round(time.time()) - round(last_activated)>=10:
                self._hero.set_shield(False)
            elif start==True and round(time.time()) - round(T1)> 2:
                self._hero.set_shield(False)
                start = False     
            self._hero.shielded()
            MAT = self._board.get_matrix()
            COPY = self._board.get_copy()
            iterator += 1
            self._rem_time = 100 - (round(time.time())-round(T1))
            if self._rem_time < 0:
                terminate("You run out of time.\n You lose. See you soon..\n")
            print('\033[0;0H')
            # time.sleep(0.6)
            # for i in range(30):
                # for j in range(204):
                    # print(bg.CYAN +" ",end ='')
                # print()
            # print('\033[0;0H')
            # time.sleep(0.001)
            # os.system('clear')

            TIME = self._rem_time
            PrintTime = [TIME // 100 , (TIME %100)// 10, (TIME%10)]
            # print("TIME REMAINING:",PrintTime[0],PrintTime[1],PrintTime[2],end ='\n')
            print("TIME REMAINING : ",PrintTime[0],end = '')
            print(PrintTime[1],end = '')
            print (PrintTime[2])

            LIVES = self._hero.get_lives()
            PrintLives = [LIVES //10 , (LIVES%10)]
            print("LIVES:",PrintLives[0],end = '')
            print(PrintLives[1])
        
            print("SCORE:",self._score,end='\n')
            print("COINS:", self._coins,end='\n')

            BOSS = self._boss.get_lives()
            PrintBoss = [BOSS // 10, BOSS%10]
            print("BOSS LIVES:",PrintBoss[0],end ='')
            print(PrintBoss[1])
            if self._hero.die(MAT) == True:
                terminate("You lost all your lives.\n You lose. See you soon..\n")
            if self._boss.die(MAT) == True:
                terminate("You win!\nYou saved Baby Yoda! See You soon..\n")
            # print(start,":::",round(time.time()) - round(T1))
            pos_hero = self._hero.get_coords()
            hero_x = pos_hero[0]
            hero_y = pos_hero[1]
            ALLOW=self._hero.get_allowed()
            UP=ALLOW[0]
            DOWN=ALLOW[1]
            RIGHT=ALLOW[2]
            LEFT=ALLOW[3]
            # print(ALLOW)

            if abs(hero_x - x_mag) < 100 and x_mag<pos_x+204 and x_mag>pos_x and iterator%2 == 1 and mag_exists==True:
                self._hero.disappear(MAT,COPY)
                MAT = self._board.get_matrix()
                COPY = self._board.get_copy()
                self._hero.attract(x_mag,y_mag)
                X=self._hero.position(MAT,COPY)
                self._coins += X[0]
                self._speedup = self._speedup or X[1]
                self._board.set_matrix(MAT)
                self._board.set_copy(COPY)

            elif abs(hero_x-x_mag) < 100 and x_mag<pos_x+204 and x_mag>pos_x and mag_exists == True:
                self._hero.set_attracted(True)
            else:
                self._hero.set_attracted(False)       # enables gravity
            
            gravity=fall_at_time//2 + 1
            inp=getinp()
            if inp == 'q':
                # QUIT
                terminate("See You Soon...")

            elif inp == '7':
                ### HACKS !!!!!
                pos_x = dims[1] - 190

            elif inp == ' ':
                #### SHIELD
                # print("SHIELD!")
                if last_activated == None  or round(time.time()) - round(last_activated) >= 60+10:
                    self._hero.set_shield(True)
                    last_activated = time.time()
                else:
                    print("RECHARGING SHIELD!!")

            elif inp == 'w' :
                # Jump
                if UP==True:
                    MAT = self._board.get_matrix()
                    COPY = self._board.get_copy()
                    self._hero.disappear(MAT,COPY)
                    self._hero.set_moving(True)
                    pos_hero = self._hero.get_coords()
                    hero_x = pos_hero[0]
                    hero_y = pos_hero[1]-1
                    if hero_y <0:
                        hero_y=0
                    self._hero.set_coords(hero_x,hero_y)
                    X=self._hero.position(MAT,COPY)
                    self._coins+=X[0]
                    self._speedup = self._speedup or X[1]
                else:
                    MAT = self._board.get_matrix()
                    COPY = self._board.get_copy()
                    pos_hero = self._hero.get_coords()
                    hero_x = pos_hero[0]
                    hero_y = pos_hero[1]
                    for i in range(hero_size[0]):
                        if MAT[hero_y-1][hero_x+i] not in not_damage:
                            if self._hero.get_shield()==False:
                                self._hero.set_lives(self._hero.get_lives()-1)
                            self._hero.disappear(MAT,COPY)
                            if MAT[hero_y-1][hero_x+i] == '*':    ## ZAPPER
                                Z.erase_zapper(MAT,COPY,hero_x+i,hero_y-1)
                            elif MAT[hero_y-1][hero_x+i] == 'M':    ## MAGNET
                                MAT[hero_y-1][hero_x+i] = ' '
                                COPY[hero_y-1][hero_x+i] = ' '
                                mag_exists=False
                            # elif MAT[hero_y-1][hero_x+i] == 'P':
                            #     MAT[hero_y-1][hero_x+i] = ' '
                            #     COPY[hero_y-1][hero_x+i] = ' '
                            #     self._speedup = True
                            #     self._board.set_speed(self._board.get_speed()+1) 
                            time.sleep(0.01)
                            X=self._hero.position(MAT,COPY)
                            self._coins+=X[0]
                            self._speedup = self._speedup or X[1]
                            ### invincibility
                            self._board.set_matrix(MAT)
                            self._board.set_copy(COPY)
                            # MAT = self._board.get_matrix()
                            # COPY = self._board.get_copy()
                            # pos_hero = self._hero.get_coords()
                            # hero_x = pos_hero[0]
                            # hero_y = pos_hero[1]
                            break

            elif inp == 'a':
                # Go Left
                if LEFT == True:
                    MAT = self._board.get_matrix()
                    COPY = self._board.get_copy()
                    self._hero.disappear(MAT,COPY)
                    self._hero.set_moving(True)
                    self._hero.set_direction(-1)
                    self._hero.set_coords(self._hero.get_coords()[0]-1,self._hero.get_coords()[1])
                    X=self._hero.position(MAT,COPY)
                    self._coins+=X[0]
                    self._speedup = self._speedup or X[1]

                else:
                    MAT = self._board.get_matrix()
                    COPY = self._board.get_copy()
                    pos_hero = self._hero.get_coords()
                    hero_x = pos_hero[0]
                    hero_y = pos_hero[1]
                    for i in range(hero_size[1]):
                        if MAT[hero_y+i][hero_x-1] not in not_damage:
                            if self._hero.get_shield()==False:
                                self._hero.set_lives(self._hero.get_lives() -1)
                            self._hero.disappear(MAT,COPY)
                            if MAT[hero_y+i][hero_x-1] == '*':    ## ZAPPER
                                Z.erase_zapper(MAT,COPY,hero_x-1,hero_y+i)
                            elif MAT[hero_y+i][hero_x-1] == 'M':
                                MAT[hero_y+i][hero_x-1] = ' '
                                COPY[hero_y+i][hero_x-1] = ' '
                                mag_exists=False
                            # elif MAT[hero_y-1][hero_x+i] == 'P':
                            #     MAT[hero_y-1][hero_x+i] = ' '
                            #     COPY[hero_y-1][hero_x+i] = ' '
                            #     self._speedup = True
                            #     self._board.set_speed(self._board.get_speed()+1) 
                            
                            time.sleep(0.01)
                            X=self._hero.position(MAT,COPY)
                            self._coins+=X[0]
                            self._speedup=self._speedup or X[1] 
                            self._board.set_matrix(MAT)
                            self._board.set_copy(COPY)
                            ### invincibility
                            break

            elif inp == 'd':
                # Go right 
                if RIGHT==True:
                    MAT = self._board.get_matrix()
                    COPY = self._board.get_copy()
                    pos_hero = self._hero.get_coords()
                    hero_x = pos_hero[0]
                    hero_y = pos_hero[1]        
                    self._hero.disappear(MAT,COPY)
                    self._hero.set_moving(True)
                    self._hero.set_direction(1)
                    self._hero.set_coords(hero_x +1,hero_y)
                    pos_hero = self._hero.get_coords()
                    hero_x = pos_hero[0]
                    hero_y = pos_hero[1]        
                    self._hero.check_collision(MAT)
                    ALLOW=self._hero.get_allowed()
                    UP=ALLOW[0]
                    DOWN=ALLOW[1]
                    RIGHT=ALLOW[2]
                    LEFT=ALLOW[3]
                    if RIGHT==True:
                        self._hero.set_coords(hero_x+1,hero_y)
                        X=self._hero.position(MAT,COPY)
                        self._coins += X[0]
                        self._speedup =self._speedup or X[1]
                        self._board.set_matrix(MAT)
                        self._board.set_copy(COPY)
                        pos_hero = self._hero.get_coords()
                        hero_x = pos_hero[0]
                        hero_y = pos_hero[1] 
                        ALLOW=self._hero.get_allowed()
                        UP=ALLOW[0]
                        DOWN=ALLOW[1]
                        RIGHT=ALLOW[2]
                        LEFT=ALLOW[3]
                        X=self._hero.position(MAT,COPY)
                        self._coins+=X[0]
                        self._speedup = self._speedup or X[1]
                        if self._speedup == True:
                            if RIGHT == True:
                                MAT = self._board.get_matrix()
                                COPY = self._board.get_copy()        
                                self._hero.disappear(MAT,COPY)
                                self._hero.set_moving(True)
                                self._hero.set_direction(1)
                                self._hero.set_coords(hero_x +1,hero_y)
                                pos_hero = self._hero.get_coords()
                                hero_x = pos_hero[0]
                                hero_y = pos_hero[1]        
                                self._hero.check_collision(MAT)
                                ALLOW=self._hero.get_allowed()
                                X=self._hero.position(MAT,COPY)
                                self._coins+=X[0]
                                self._speedup = self._speedup or X[1]
                                UP=ALLOW[0]
                                DOWN=ALLOW[1]
                                RIGHT=ALLOW[2]
                                LEFT=ALLOW[3]
                                            
                            else:
                                for i in range(hero_size[1]):
                                    if MAT[hero_y+i][hero_x+hero_size[0]] not in not_damage :
                                        if self._hero.get_shield()==False:
                                            self._hero.set_lives(self._hero.get_lives()-1)
                                        pos_hero = self._hero.get_coords()
                                        hero_x = pos_hero[0]
                                        hero_y = pos_hero[1]        
                                        if MAT[hero_y+i][hero_x+hero_size[0]] == '*':    ## ZAPPER
                                            Z.erase_zapper(MAT,COPY,hero_x+hero_size[0],hero_y+i)
                                        elif MAT[hero_y+i][hero_x+hero_size[0]] == 'M':
                                            MAT[hero_y+i][hero_x+hero_size[0]] = ' '
                                            COPY[hero_y+i][hero_x+hero_size[0]] = ' '
                                            mag_exists = False
                                        # elif MAT[hero_y-1][hero_x+i] == 'P':
                                        #     # print("YE")
                                        #     MAT[hero_y-1][hero_x+i] = ' '
                                        #     COPY[hero_y-1][hero_x+i] = ' '
                                        #     self._speedup = True
                                        #     self._board.set_speed(self._board.get_speed()+1) 
                            
                                        time.sleep(0.01)
                                        X=self._hero.position(MAT,COPY)
                                        self._coins+=X[0]
                                        self._speedup = self._speedup or X[1]
                                        break
                    else:
                        for i in range(hero_size[1]):
                            if MAT[hero_y+i][hero_x+hero_size[0]] not in not_damage :
                                if self._hero.get_shield()==False:
                                    self._hero.set_lives(self._hero.get_lives()-1)
                                pos_hero = self._hero.get_coords()
                                hero_x = pos_hero[0]
                                hero_y = pos_hero[1]        
                                if MAT[hero_y+i][hero_x+hero_size[0]] == '*':    ## ZAPPER
                                    Z.erase_zapper(MAT,COPY,hero_x+hero_size[0],hero_y+i)
                                elif MAT[hero_y+i][hero_x+hero_size[0]] == 'M':
                                    MAT[hero_y+i][hero_x+hero_size[0]] = ' '
                                    COPY[hero_y+i][hero_x+hero_size[0]] = ' '
                                    mag_exists = False
                                # elif MAT[hero_y-1][hero_x+i] == 'P':
                                #     MAT[hero_y-1][hero_x+i] = ' '
                                #     COPY[hero_y-1][hero_x+i] = ' '
                                #     self._speedup = True
                                #     self._board.set_speed(self._board.get_speed()+1) 
                                
                                time.sleep(0.01)
                                X=self._hero.position(MAT,COPY)
                                self._coins +=X[0]
                                self._speedup = self._speedup or X[1]
                                break
                                #invincibility
                    self._board.set_matrix(MAT)
                    self._board.set_copy(COPY)
                else:
                    # print("!")
                    # time.sleep(1)
                    MAT = self._board.get_matrix()
                    COPY = self._board.get_copy()
                    pos_hero = self._hero.get_coords()
                    hero_x = pos_hero[0]
                    hero_y = pos_hero[1]        
                    for i in range(hero_size[1]):
                        if MAT[hero_y+i][hero_x+hero_size[0]] not in not_damage:
                            if self._hero.get_shield()==False:
                                self._hero.set_lives(self._hero.get_lives() -1)
                            self._hero.disappear(MAT,COPY)
                            if MAT[hero_y+i][hero_x+hero_size[0]] == '*':    ## ZAPPER
                                Z.erase_zapper(MAT,COPY,hero_x+hero_size[0],hero_y+i)
                            elif MAT[hero_y+i][hero_x+hero_size[0]] == 'M':
                                MAT[hero_y+i][hero_x+hero_size[0]] = ' '
                                COPY[hero_y+i][hero_x+hero_size[0]] = ' '
                                mag_exists = False
                            # elif MAT[hero_y-1][hero_x+i] == 'P':
                            #     MAT[hero_y-1][hero_x+i] = ' '
                            #     COPY[hero_y-1][hero_x+i] = ' '
                            #     self._speedup = True
                            #     self._board.set_speed(self._board.get_speed()+1) 
                            time.sleep(0.01)
                            X=self._hero.position(MAT,COPY)
                            self._coins += X[0]
                            self._speedup = self._speedup or X[1]
                            ### invincibility        
                            self._board.set_matrix(MAT)
                            self._board.set_copy(COPY)
                            break

            elif inp == 'k':
                ## FIRE BULLET
                pos_hero = self._hero.get_coords()
                hero_x = pos_hero[0]
                hero_y = pos_hero[1]

                self._fired_bullets += [Bullet(hero_x+self._board.get_speed(),hero_y+self._board.get_speed(),self._hero.get_direction())]

            else:
                self._hero.set_moving(False)


                        #### UPDATE NECESSARY 
            MAT = self._board.get_matrix()
            COPY = self._board.get_copy()
            pos_hero = self._hero.get_coords()
            hero_x = pos_hero[0]
            hero_y = pos_hero[1]
            ALLOW=self._hero.get_allowed()
            UP=ALLOW[0]
            DOWN=ALLOW[1]
            RIGHT=ALLOW[2]
            LEFT=ALLOW[3]        

            if RIGHT==False and hero_x == pos_x:          #### CHECK
                for i in range(hero_size[1]):
                    if MAT[hero_y+i][hero_x+hero_size[0]] not in not_damage:
                        if self._hero.get_shield()==False:
                            self._hero.set_lives(self._hero.get_lives() -1)
                        self._hero.disappear(MAT,COPY)
                        if MAT[hero_y+i][hero_x+hero_size[0]] == '*':    ## ZAPPER
                            Z.erase_zapper(MAT,COPY,hero_x+hero_size[0],hero_y+i)
                            # time.sleep(3)
                        elif MAT[hero_y+i][hero_x+hero_size[0]] == 'M':
                            # MAT[hero_y+i][[hero_x+hero_size[0]] = ' '
                            self._board.Place(hero_x + hero_size[0],hero_x + hero_size[0] ,hero_y+i,hero_y+i, ' ')
                            self._board.PlaceCopy(hero_x + hero_size[0],hero_x + hero_size[0], hero_y +i,hero_y +i, ' ')                                    
                            mag_exists = False
                        # elif MAT[hero_y-1][hero_x+i] == 'P':
                        #     MAT[hero_y-1][hero_x+i] = ' '
                        #     COPY[hero_y-1][hero_x+i] = ' '
                        #     self._board.set_speed(self._board.get_speed()+1) 
                        #     self._speedup = True
                            
                        time.sleep(0.01)
                        X=self._hero.position(MAT,COPY)
                        self._coins += X[0]
                        self._speedup = self._speedup or X[1]
                        self._board.set_matrix(MAT)
                        self._board.set_copy(COPY)
                        ### invincibility            
                        break

            MAT = self._board.get_matrix()
            COPY = self._board.get_copy()
            
            for ii in self._fired_bullets:
                x=ii.Update_bullet(MAT,COPY,dims[1],pos_x)
                if x == True:
                    self._fired_bullets.remove(ii)
                elif x == None:
                    pass
                else:
                    # print(x)
                    # time.sleep(1)
                    y=Z.erase_zapper(MAT,COPY,x[0]+ii.get_direction(),x[1])
                    if y == False:    # zapper not found, i.e. boss 
                        if MAT[x[1]][x[0]+ii.get_direction()]== 'M':
                            # print("MAG DESTR")
                            # sleep(1)
                            MAT[x[1]][x[0]+ii.get_direction()] = ' '
                            # COPY[x[1]][x[0]+ii.direction] = ' '     ### CHECK
                            self._fired_bullets.remove(ii)
                            del ii
                            mag_exists = False
                        
                        elif MAT[x[1]][x[0]+ii.get_direction()]=='o' or MAT[x[1]][x[0]+ii.get_direction()+1]=='o':     # or MAT[x[1]][x[0]+ii.get_direction()]==fg.RED+'o'
                            # print("SNOWBALLL DESTR")
                            MAT[x[1]][x[0]+ii.get_direction()] = ' '
                            self._fired_bullets.remove(ii)
                            del ii
                        
                        elif dims[1] - x[0] < 190  and x[0]>=self._boss.get_coords()[0] and MAT[x[1]][x[0]+ii.get_direction()]!='o':
                            self._boss.set_lives(self._boss.get_lives()- 1)
                        
            self._board.set_matrix(MAT)
            self._board.set_copy(COPY)

            ALLOW=self._hero.get_allowed()
            UP=ALLOW[0]
            DOWN=ALLOW[1]
            RIGHT=ALLOW[2]
            LEFT=ALLOW[3]

            if inp != 'w' and DOWN==True and self._hero.get_attracted()==False: # as long as you hold no up  gravity ; If allowed_down is False, then don t allow to come down;mag overcomes gravity also
                cntr=0
                self._hero.disappear(MAT,COPY)
                # if self.hero.falling == True:         # checks if falling (i.e. gravity is acting)
                while cntr<gravity and DOWN==True:
                    self._hero.fall(1)
                    self._hero.check_collision(MAT)
                    ALLOW=self._hero.get_allowed()
                    DOWN=ALLOW[1]
                    cntr+=1
                    X=self._hero.position(MAT,COPY)
                    self._coins+=X[0]
                    self._speedup = self._speedup or X[1]
                    self._hero.disappear(MAT,COPY)
                fall_at_time+=1                     # increments time of falling
                X=self._hero.position(MAT,COPY)
                self._coins+=X[0]
                self._speedup = self._speedup or X[1]
                # else:
            else:
                fall_at_time=0

            ALLOW=self._hero.get_allowed()
            UP=ALLOW[0]
            DOWN=ALLOW[1]
            RIGHT=ALLOW[2]
            LEFT=ALLOW[3]
            MAT = self._board.get_matrix()
            COPY = self._board.get_copy()
            pos_hero = self._hero.get_coords()
            hero_x = pos_hero[0]
            hero_y = pos_hero[1]

            if DOWN==False and inp!='w':      # downward collision check
                for i in range(hero_size[0]):
                    if MAT[hero_y+hero_size[0]][hero_x+i] not in not_damage:
                        if self._hero.get_shield()==False:
                            self._hero.set_lives(self._hero.get_lives()-1)
                        self._hero.disappear(MAT,COPY)
                        if MAT[hero_y+hero_size[1]][hero_x+i] == '*':    ## ZAPPER
                            Z.erase_zapper(MAT,COPY,hero_x+i,hero_y+hero_size[1])
                        elif MAT[hero_y+hero_size[1]][hero_x+i] == 'M':
                            # self.board.matrix[self.hero.y_coord+self.hero.size_y][self.hero.x_coord+i] = ' '
                            self._board.Place(hero_x + i,hero_x + i ,hero_y+hero_size[1],hero_y+hero_size[1], ' ')
                            self._board.PlaceCopy(hero_x + i,hero_x + i, hero_y +hero_size[1],hero_y +hero_size[1], ' ')      
                            mag_exists=False
                        time.sleep(0.01)
                        X=self._hero.position(MAT,COPY)
                        self._coins += X[0]
                        self._speedup =self._speedup or X[1]
                        self._board.set_matrix(MAT)
                        self._board.set_copy(COPY)
                        
                        ### invincibility            
                        break

            ALLOW=self._hero.get_allowed()
            UP=ALLOW[0]
            DOWN=ALLOW[1]
            RIGHT=ALLOW[2]
            LEFT=ALLOW[3]
            MAT = self._board.get_matrix()
            COPY = self._board.get_copy()
            pos_hero = self._hero.get_coords()
            hero_x = pos_hero[0]
            hero_y = pos_hero[1]
            self._hero.disappear(MAT,COPY)

            if RIGHT==True or hero_x != pos_x:
                pos_x+=self._board.get_speed()

            if hero_y<0:
                hero_y=0

            if hero_x < pos_x:
                hero_x = pos_x
                
            elif hero_x + 3 > pos_x + 204 :    # at a time 204 columns.
                hero_x = pos_x + 204 - 3

            self._hero.set_coords(hero_x,hero_y)

            X=self._hero.position(MAT,COPY)
            self._coins += X[0]
            self._speedup =self._speedup or X[1]
            self._board.set_matrix(MAT)
            self._board.set_copy(COPY)            
            MAT = self._board.get_matrix()
            COPY = self._board.get_copy()
            pos_hero = self._hero.get_coords()
            hero_x = pos_hero[0]
            hero_y = pos_hero[1]
            cols_over=self._board.PrintBoard(pos_x)
            if (RIGHT==True or hero_x !=pos_x) and cols_over == True: ## CHECK THIS FURTHER. What exactly happens at the end of the board. SHUD THIS BE POSITIONED NEAR POS_X+=SPEED ? HOw why?
                pos_x -= self._board.get_speed()
            self._hero.check_collision(MAT)

            ALLOW=self._hero.get_allowed()
            UP=ALLOW[0]
            DOWN=ALLOW[1]
            RIGHT=ALLOW[2]
            LEFT=ALLOW[3]
            pos_hero = self._hero.get_coords()
            hero_x = pos_hero[0]
            hero_y = pos_hero[1]

            
            if abs( self._boss.get_coords()[0] - hero_x )<150:
                self._boss.fight(self._hero,MAT,COPY)
                x=random.randint(0,15)
                if iterator% 5 == 0 and self._boss.get_lives()>0:
                    self._thrown_snowballs+=[Snowball(self._boss.get_coords()[0],self._boss.get_coords()[1]+x)]
                for ii in self._thrown_snowballs:
                    x=ii.Update_snowball(MAT,COPY,pos_x)
                    if x == True:
                        self._thrown_snowballs.remove(ii)
                    elif x == None:
                        pass
                    else:
                        if MAT[x[1]][x[0]-1] in ['^','\\','/','|']:
                            if self._hero.get_shield()==False:
                                self._hero.set_lives(self._hero.get_lives()-1)
                            self._hero.disappear(MAT,COPY)
                            time.sleep(0.01)
                            X=self._hero.position(MAT,COPY)
                            self._coins+=X[0]
                            self._speedup =self._speedup or X[1]
                            self._board.set_matrix(MAT)
                            self._board.set_copy(COPY)

                            ### NO invincibility. That is the challenge.
        




