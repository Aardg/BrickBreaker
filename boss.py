from colorama import Fore, Back, Style
from os import system, name
from time import sleep
from os import system
import object

class boss(object.object):

    def __init__(self,x,y):
        self._x=x
        self._y=y
        self._w=13
        self._h=6
        self._img=[
            [" "," "," "," ",4,4,4,4,4," "," "," "," "],
            [" "," "," "," ",4," "," "," ",4," "," "," "," "],
            [4,4,4,4,4,"\u2629","\u2629","\u2629",4,4,4,4,4],
            [4,"\u229B","\u229B","\u229B",4,4,4,4,4,"\u229B","\u229B","\u229B",4],
            [4,4,4,4,4,4,4,4,4,4,4,4,4],
            [" "," "," "," ",4," "," "," ",4," "," "," "," "]
        ]
        self.life=50

    def move_onscreen(self,board,inp):
        system('clear')
        
        if inp == 'a':
            if(self._x-1>2 ):
                self.remove_onscreen(board)
                if self._x - 1 > 0:
                    self._x-=1
                
        if inp == 'd':
            if(self._x+self._w < 49 ):
                self.remove_onscreen(board)
                if self._x + self._w  < 49:
                    self._x+=1  
        self.print_onscreen(board)