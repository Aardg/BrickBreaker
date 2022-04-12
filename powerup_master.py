from colorama import Fore, Back, Style
from os import system, name
from time import sleep
from os import system
import global_stuff
import object
import collisions

power_duration=global_stuff.power_duration

class powerup(object.object):

    def __init__(self,x,y,effect):
        
        self._x=x
        self._y=y
        self._h=1   
        self._w=1
        if effect == 1:
            self._img=[["B"]]
        if effect == 2:
            self._img=[["S"]]
        if effect == 3:
            self._img=[["F"]]
        if effect == 4:
            self._img = [["D"]]
        if effect == 5:
            self._img = [["G"]]
        if effect == 6:
            self._img = [["P"]]
        
        self._xv=0
        self._yv=1
        self.spawned = 0
        self._effect = effect
        self.time = 0

    def collected(self, board):

            if self._y + 1 > 48:
                self.spawned=0
                self._img=[[" "]]
                return

            else:
                for i in range(self._yv):
                    if int(self._y)+1+i > 49:
                        self.spawned=0
                        return -1

                    if board[int(self._y)+1+i][int(self._x)] == "=" or board[int(self._y)+1+i][int(self._x)] == "!":
                        self.remove_onscreen(board)
                        self.spawned = 0
                        power_duration[self._effect-1]+=150
                        if self._effect == 1:
                            power_duration[1]=0
                        if self._effect == 2:
                            power_duration[0]=0
                        return self._effect

    def move_powerup(self,board):


        self.remove_onscreen(board)
        fl=collisions.pp_wall(self,board)
        # collisions.pp_brick(self,board)

        self._y+=self._yv

        self.time+=1
        if self.time==10:
            self._yv+=1
            self.time=0
        if fl==1:
            self._x+=self._xv
            self._y-=self._yv
        if fl==-1:
            
            self.spawned=0
            for i in range(1,49):
                board[48][i]=" "
            self.remove_onscreen(board)

            return self.collected(board)

        self.print_onscreen(board)

        return self.collected(board)
        
    def fall(self,board):

        self.remove_onscreen(board)
        self._y+=1
    
