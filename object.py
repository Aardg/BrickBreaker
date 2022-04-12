from colorama import Fore, Back, Style
from os import system, name
from time import sleep
from os import system

class object:
    
    def __init__(self,x,y,h,w,img):
        self._x=x
        self._y=y
        self._h=h
        self._w=w
        self._img=img 
    
    def print_onscreen(self, board):

        if(self._x+self._w<50 and self._y + self._h<50 and self._x>0 and self._y>0):
            for i in range(self._h):
                for j in range(self._w):
                    board[int(self._y+i)][int(self._x + j)]=self._img[i][j]
    
    def remove_onscreen(self,board):
        
        for i in range(self._h):
            for j in range(self._w):
                if self._y+i < 50 and self._y+i > 0  and self._x+j < 50 and self._x+j > 0:
                    board[int(self._y+i)][int(self._x + j)]=" "
                
    
                

                