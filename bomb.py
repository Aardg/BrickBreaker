from colorama import Fore, Back, Style
from os import system, name
from time import sleep
from os import system
import collisions
import object

import collisions

class bomb(object.object):

    def __init__(self,x,y,yv,dmg):
        
        self._x=x
        self._y=y
        self._h=1
        self._w=1
        self._img=[["A"]]
        self._xv=0
        self._yv=yv
        self._dmg=dmg
        
    def move_bomb(self,board):

        self.remove_onscreen(board)
        self._y-=self._yv
        if self._y==48:  
            return -1
        self.print_onscreen(board)

        return collisions.bomb_paddle(self,board)

        

    