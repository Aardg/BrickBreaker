from colorama import Fore, Back, Style
from os import system,name
from time import sleep
from os import system
import global_stuff
import object
import os
import collisions


class ball(object.object):
    def __init__(self,x,y,life,dmg):
        self._x=x
        self._y=y
        self._h=1
        self._w=1
        self._img=[["\u2B24"]]
        self._xv=1
        self._yv=1
        self._life=life
        self._dmg=dmg

    def move_ball(self,board):

        if global_stuff.level!=3:
            system('clear')
            fl=collisions.ball_wall(self,board)


            
            self._y-=self._yv

            if fl==1:
                self._x+=self._xv
                os.system("aplay ./sounds/1.wav &")

            if fl==-1:
                return -1

            if self._y > 45:
                collisions.ball_paddle(self,board)

            return collisions.ball_brick(self,board)

        else:
            system('clear')
            fl=collisions.ball_wall(self,board)
            hit=collisions.ball_boss(self,board)

        


            self._y-=self._yv

            if fl==1:
                self._x+=self._xv
                os.system("aplay ./sounds/1.wav &")

            if fl==-1:
                return -1

            if self._y > 45:
                collisions.ball_paddle(self,board)
            return hit
            

    def increasexv(self,newxv):

        self._xv+=newxv
        return

    def increasedmg(self,newdmg):

        self._dmg=newdmg
        return 

    def retdmg(self):

        return self._dmg
    
    def resetdmg():
        self._dmg=1