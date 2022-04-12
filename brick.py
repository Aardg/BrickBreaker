from colorama import Fore, Back, Style
from os import system, name
from time import sleep
from os import system
import object

class brick(object.object):

    def __init__(self,x,y,h,w,img,str):
        
        self._str=str
        if self._str == 0:
            img = [[' ']*3]
        elif self._str == 1:
            img = [[1]*3]
        elif self._str == 2:
            img = [[2]*3]
        elif self._str == 3:
            img = [[3]*3]
        else:
            img = [[4]*3]
        
        self.touched=0
        super().__init__(x,y,h,w,img)
    
    def ret_str(self):

        return self._str
    
    def ret_pos(self):
        
        return (int(self._x),int(self._y))
    
    def fall(self,board):

        self.remove_onscreen(board)
        self._y+=1  
        
