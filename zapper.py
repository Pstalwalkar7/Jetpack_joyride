import random
class Zapper:
    
    def __init__(self,x,y):
        self.__x_coord = x
        self.__y_coord = y 
        self.__token = '*'
    
    def create_zapper(self,board):
        form  = random.randint(1,6)
        dim = board.get_dims()
        flag = True
        start_x = self.__x_coord
        start_y = self.__y_coord
        if form in [1,2]:    # horizontal
            end_x = start_x + 7 
            if end_x >= dim[1]:
                end_x = dim[1] - 1

            flag = board.check_empty(start_x,end_x,start_y,start_y)

            if flag == True:
                board.Place(start_x,end_x,start_y,start_y,self.__token)

        elif form in [3,4]:    # vertical
            end_y=start_y + 15
            if end_y >= 27:
                end_y = 27 - 1

            flag = board.check_empty(start_x,start_x,start_y,end_y)

            if flag ==  True:
                board.Place(start_x,start_x,start_y,end_y,self.__token)
            
        elif form == 5:
            end_x = start_x + 10 
            end_y = start_y + 10
            if end_x >= dim[1] :
                end_x = dim[1] - 1
            if end_y >= 27:
                end_y = 27 -1
            
            minidiff=end_x-start_x if (end_x - start_x < end_y - start_y) else end_y-start_y
            flag = board.a8_h1_empty(start_x,start_y,minidiff)

            if flag == True:
                board.a8_h1_fill(start_x,start_y,minidiff,self.__token) 

        elif form ==6:
            end_x = start_x - 10
            end_y = start_y + 10
            if end_x < 0:
                end_x = 0
            if end_y >= 27 :
                end_y = 27 -1

            minidiff = start_x - end_x if (start_x - end_x < end_y - start_y) else end_y - start_y
            flag = board.h8_a1_empty(start_x,start_y,minidiff)

            if flag == True:
                board.h8_a1_fill(start_x,start_y,minidiff,self.__token)

        else:
            print("NOT POSSIBLE")

        return flag

    def erase_zapper(self,MAT,COPY,start_x,start_y):
        copy_x = start_x
        copy_y = start_y
        success = False

        if MAT[start_y][start_x+1] == '*':    # Horizontal L->R
            success=True
            while MAT[start_y][start_x] == '*':
                MAT[start_y][start_x] = ' '
                COPY[start_y][start_x] = ' '
                start_x += 1

        elif MAT[start_y+1][start_x] == '*':    # Vertical   U->D
            success=True
            while MAT[start_y][start_x] == '*':
                MAT[start_y][start_x] = ' '
                COPY[start_y][start_x] = ' '
                start_y += 1
            
        elif MAT[start_y+1][start_x+1] == '*':   # form=5     a8 to h1 as white
            success=True
            while MAT[start_y][start_x] == '*':
                MAT[start_y][start_x] = ' '
                COPY[start_y][start_x] = ' '
                start_y +=1
                start_x +=1

        elif MAT[start_y+1][start_x-1] == '*':    # form = 6    h8 to a1 as white
            success=True
            while MAT[start_y][start_x] == '*':
                MAT[start_y][start_x] = ' '
                COPY[start_y][start_x] = ' '
                start_y +=1
                start_x -=1

        else:         # causes the boss to flicker
            if MAT[start_y][start_x]=='*':
                success=True
            MAT[start_y][start_x]=' '
            COPY[start_y][start_x] = ' '

        if MAT[copy_y][copy_x - 1] == '*':       # Horizontal r->l
            success=True
            copy_x -=1
            while MAT[copy_y][copy_x] =='*':
                MAT[copy_y][copy_x] = ' '
                COPY[copy_y][copy_x] = ' '
                copy_x -=1

        elif copy_y>0 and MAT[copy_y-1][copy_x] =='*':       # vertical d->u
            success=True
            copy_y-=1
            while copy_y>=0 and MAT[copy_y][copy_x] == '*':
                MAT[copy_y][copy_x] = ' '
                COPY[copy_y][copy_x] = ' '
                copy_y -=1

        elif copy_y>0 and MAT[copy_y-1][copy_x-1] == '*':    # form=5 h1 to a8
            success=True
            copy_x -=1
            copy_y -=1
            while copy_y>=0 and MAT[copy_y][copy_x] == '*':
                MAT[copy_y][copy_x] = ' '
                COPY[copy_y][copy_x] = ' '
                copy_x -= 1
                copy_y -= 1

        elif copy_y>0 and MAT[copy_y-1][copy_x +1] == '*':    # form =6 , a1 to h8
            success=True
            copy_x+=1
            copy_y -=1
            while copy_y>=0 and MAT[copy_y][copy_x] == '*':
                MAT[copy_y][copy_x] = ' '
                COPY[copy_y][copy_x] = ' '
                copy_x += 1
                copy_y -= 1

        else:
            pass

        return success
