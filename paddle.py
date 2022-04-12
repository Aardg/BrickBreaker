from colorama import Fore, Back, Style
from os import system, name
from time import sleep
from os import system
import object

class paddle(object.object):
    
    def returnxy(self):
        return (self._x,self._y)
        
    def move_paddle(self, board, inp):  
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