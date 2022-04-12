import paddle
import brick
import ball 
import numpy as np
import inp
import global_stuff
import powerup_master

board= np.array([[" "]*50]*50)
bricks2 = [""]*45
bricks1 = [""]*45

pp1 = [""]*45
pp2 = [""]*45

paddle=paddle.paddle(25,48,1,5,[["="]*5])
balls = ball.ball(25,47,30,1)

pos1 = global_stuff.pos1
pos2 = global_stuff.pos2

pppos1 = global_stuff.pppos1
pppos2 = global_stuff.pppos2


for i in range(36):

    if i%3 == 0:
        bricks1[i] = brick.brick(pos1[i][1],pos1[i][0],1,3,[[0]*3],3)
    elif i%3 == 1:
        bricks1[i] = brick.brick(pos1[i][1],pos1[i][0],1,3,[[0]*3],2)
    elif i%3 == 2:
        bricks1[i] = brick.brick(pos1[i][1],pos1[i][0],1,3,[[0]*3],1)

for i in range(36,41):
    bricks1[i] = brick.brick(pos1[i][1],pos1[i][0],1,3,[[0]*3],100)

for i in range(36):

    if i>29:
        bricks2[i] = brick.brick(pos1[i][1],pos1[i][0],1,3,[[0]*3],0)

    elif i%3 == 0:
        bricks2[i] = brick.brick(pos2[i][1],pos2[i][0],1,3,[[0]*3],3)
    elif i%3 == 1:
        bricks2[i] = brick.brick(pos2[i][1],pos2[i][0],1,3,[[0]*3],2)
    elif i%3 == 2:
        bricks2[i] = brick.brick(pos2[i][1],pos2[i][0],1,3,[[0]*3],1)

for i in range(36,41):
    bricks2[i] = brick.brick(pos2[i][1],pos2[i][0],1,3,[[0]*3],100)

for i in range(41):
    pp2[i] = powerup_master.powerup(pos2[i][1],pos2[i][0],(i%6)+1)

for i in range(41):
    pp1[i] = powerup_master.powerup(pos1[i][1],pos1[i][0],(i%6)+1)
