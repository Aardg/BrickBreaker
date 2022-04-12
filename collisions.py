from colorama import Fore, Back, Style
from os import system, name
from time import sleep
from os import system
import global_stuff


score=global_stuff.score
powerup_duration = global_stuff.power_duration

def ball_wall(ball,board):


    if global_stuff.level==2:
        pos=global_stuff.pos2
    elif global_stuff.level==1:
        pos=global_stuff.pos1

    if ball._y < 2:
        ball._yv*=-1

    if ball._y > 49:
        ball._life-=1
        ball._x=25
        ball._y=40
        ball._yv=1
        ball._xv=1
        for i in range(6):
            powerup_duration[i]=0
            
        if ball._life == 0:
            system('clear')
            print('GAME OVER')
            exit()

        return -1

    ball.remove_onscreen(board)

    for i in range(abs(ball._xv)):
        if ball._x > 47 :
            ball._xv=ball._xv*(-1)
            ball.remove_onscreen(board)
            return 1

        elif  ball._x < 3:
            ball._xv=ball._xv*(-1)
            ball.remove_onscreen(board)
            return 1
        
        ball._x+=1*(ball._xv/abs(ball._xv))
        

def ball_paddle(ball,board):

    if global_stuff.level==2:
        pos=global_stuff.pos2
    elif global_stuff.level==1:
        pos=global_stuff.pos1

    if ball._y > 48:
        return

    else:

        global_stuff.onpaddle=1
        if  board[int(ball._y)+1][int(ball._x)] == "=" or board[int(ball._y)+1][int(ball._x)] == "!":
            ball._yv = (-1)*ball._yv
            i=0

            while board[int(ball._y) + 1][int(ball._x)-i]=="=" or  board[int(ball._y) + 1][int(ball._x)-i]=="!":
                i+=1
            
            if i<3:
                ball._xv-=1
            elif i>3:
                ball._xv+=1

            return
    

def weaken(contact): 

    if global_stuff.level==1:
        pos=global_stuff.pos1   

    if global_stuff.level==2:
        pos=global_stuff.pos2

    fl=-1
    i=0
    while i in range(5):
        
        if (contact[0], contact[1]-i) in pos:
            fl=pos.index((contact[0], contact[1]-i))

            return fl
            break
        i+=1
    return fl

def bullet_brick(bullet,board):

    if global_stuff.level==2:
        pos=global_stuff.pos2
    elif global_stuff.level==1:
        pos=global_stuff.pos1

    if board[int(bullet._y)-1][int(bullet._x)].isnumeric():
        return weaken((int(bullet._y - 1),int(bullet._x)))
    

def ball_brick(ball,board):
    
    if global_stuff.level==2:
        pos=global_stuff.pos2
    elif global_stuff.level==1:
        pos=global_stuff.pos1
    print("                                         LEVEL : ",global_stuff.level)
    
    if ball._x < 48 and ball._x > 2 and ball._y < 45 and ball._y > 2:
        if ball._xv >= 0 and ball._yv >= 0:
            
            if board[int(ball._y - 1)][int(ball._x+1)].isnumeric():
                if ball._dmg==1:
                    ball._yv*=-1
                return weaken((int(ball._y - 1),int(ball._x+1)))

            if board[int(ball._y)][int(ball._x+1)].isnumeric():
                if ball._dmg==1:
                    ball._xv*=-1
                return weaken((int(ball._y),int(ball._x+1)))

        if ball._xv >= 0 and ball._yv <= 0:

            if board[int(ball._y+1)][int(ball._x+1)].isnumeric():
                if ball._dmg==1:
                    ball._yv*=-1
                return weaken((int(ball._y + 1),int(ball._x+1)))
            
            if board[int(ball._y)][int(ball._x+1)].isnumeric():
                if ball._dmg==1:
                    ball._xv*=-1
                return weaken((int(ball._y),int(ball._x+1)))
        
        if ball._xv <= 0 and ball._yv >= 0:

            if board[int(ball._y-1)][int(ball._x-1)].isnumeric():
                if ball._dmg==1:
                    ball._yv*=-1
                return weaken((int(ball._y - 1),int(ball._x-1)))
            
            if board[int(ball._y)][int(ball._x-1)].isnumeric():
                if ball._dmg==1:
                   ball._xv*=-1
                return weaken((int(ball._y),int(ball._x-1)))

        if ball._xv <= 0 and ball._yv <= 0:

            if board[int(ball._y+1)][int(ball._x-1)].isnumeric():
                if ball._dmg==1:
                    ball._yv*=-1
                return weaken((int(ball._y + 1),int(ball._x - 1)))

            if board[int(ball._y)][int(ball._x-1)].isnumeric():
                if ball._dmg==1:
                    ball._xv*=-1
                return weaken((int(ball._y),int(ball._x-1)))

def pp_wall(pp,board):

    if global_stuff.level==2:
        pos=global_stuff.pos2
    elif global_stuff.level==1:
        pos=global_stuff.pos1

    pp.remove_onscreen(board)

    if pp._y < 2:
        pp._yv*=-1
    if pp._y > 49:
        return -1

    for i in range(abs(pp._xv)):
        if pp._x > 47 :
            pp._xv=pp._xv*(-1)
            pp.remove_onscreen(board)
            return 1

        elif  pp._x < 3:
            pp._xv=pp._xv*(-1)
            pp.remove_onscreen(board)
            return 1
        
        pp._x+=1*(pp._xv/abs(pp._xv))

def pp_brick(pp,board):

    if global_stuff.level==2:
        pos=global_stuff.pos2
    elif global_stuff.level==1:
        pos=global_stuff.pos1

    if pp._x < 48 and pp._x > 2 and pp._y < 45 and pp._y > 2:
        if pp._xv >= 0 and pp._yv >= 0:
            
            if board[int(pp._y - 1)][int(pp._x+1)].isnumeric():
                pp._yv*=-1

            if board[int(pp._y)][int(pp._x+1)].isnumeric():
                pp._xv*=-1
                

        if pp._xv >= 0 and pp._yv <= 0:

            if board[int(pp._y+1)][int(pp._x+1)].isnumeric():
                pp._yv*=-1
            
            if board[int(pp._y)][int(pp._x+1)].isnumeric():
                pp._xv*=-1
                
        
        if pp._xv <= 0 and pp._yv >= 0:

            if board[int(pp._y-1)][int(pp._x-1)].isnumeric():
                pp._yv*=-1
            
            if board[int(pp._y)][int(pp._x-1)].isnumeric():
                pp._xv*=-1
                

        if pp._xv <= 0 and pp._yv <= 0:

            if board[int(pp._y+1)][int(pp._x-1)].isnumeric():
                pp._yv*=-1

            if board[int(pp._y)][int(pp._x-1)].isnumeric():
                pp._xv*=-1


def ball_boss(ball,board):
    
    if ball._x < 48 and ball._x > 2 and ball._y < 45 and ball._y > 2:
        if ball._xv >= 0 and ball._yv >= 0:
            
            if board[int(ball._y - 1)][int(ball._x+1)] == "4":
                ball._yv*=-1
                return 1

            if board[int(ball._y)][int(ball._x+1)] == "4":
                ball._xv*=-1
                return 1
                

        if ball._xv >= 0 and ball._yv <= 0:

            if board[int(ball._y+1)][int(ball._x+1)] == "4":
                ball._yv*=-1
                return 1

            if board[int(ball._y)][int(ball._x+1)] == "4":
                ball._xv*=-1
                return 1
                
        
        if ball._xv <= 0 and ball._yv >= 0:

            if board[int(ball._y-1)][int(ball._x-1)] == "4":
                ball._yv*=-1
                return 1
            
            if board[int(ball._y)][int(ball._x-1)] == "4":
                ball._xv*=-1
                return 1                

        if ball._xv <= 0 and ball._yv <= 0:

            if board[int(ball._y+1)][int(ball._x-1)] == "4":
                ball._yv*=-1
                return 1

            if board[int(ball._y)][int(ball._x-1)] == "4":
                ball._xv*=-1
                return 1
        return 0

    
def bomb_paddle(bomb,board):

    if board[int(bomb._y)+1][int(bomb._x)]=="=":
        return 1

    