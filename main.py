import paddle
import brick
import ball 
import numpy as np
import inp
import setup
import random
import bullet
import ball
import global_stuff
import boss
import bomb
import os
pos = global_stuff.pos1
score = global_stuff.score
pppos = global_stuff.pppos1
power_duration = global_stuff.power_duration

from os import system
from time import sleep
from colorama import Fore, Back, Style

import powerup_master

rain_brick={}
for i in range(30):
    rain_brick[i]=0
screen = setup.board
balls = setup.balls
paddles = setup.paddle
bimg='\u2B24'
bricks = setup.bricks1
pp = setup.pp1

bullets=bullet.bullet(1,1,1,1)
bmb1 = bomb.bomb(1,1,-1,1)
bmb2 = bomb.bomb(1,1,-1,1)
bmb3 = bomb.bomb(1,1,-1,1)
bmb4 = bomb.bomb(1,1,-1,1)
bmb5 = bomb.bomb(1,1,-1,1)
bmb6 = bomb.bomb(1,1,-1,1)


drop=1
for i in range(50):
    for j in range(50):
        if i == 0:
            screen[i][j] = '\u039E'
        if j==49:
            screen[i][j] = '\u039E'
        if j == 0:
            screen[i][j] = '\u039E' 
        if i == 49:
            screen[i][j] = '\u039E'


a = "asdf"
strn=3
getch = inp.Get()
safeT=0
lf=30
grab=1
time=0
bos = boss.boss(20,5)
blevel=0
while a!="q":

    if global_stuff.level==3:

        if balls._life==0:
            system('clear')
            system('clear')
            system('clear')
            system('clear')
            print("YOU LOSE")
            exit()
        
        if drop==1:
            drop=0
            bmb1=bomb.bomb(bos._x+2,bos._y,-1,1)
            bmb2=bomb.bomb(bos._x+10,bos._y,-1,1)


        if bmb1._y == 16:
            bmb3=bomb.bomb(bos._x+4,bos._y,-1,1)
            bmb4=bomb.bomb(bos._x+8,bos._y,-1,1)
    
        if bmb1._y == 32:
            bmb5=bomb.bomb(bos._x+6,bos._y,-1,1)
            bmb6=bomb.bomb(bos._x+12,bos._y,-1,1)


        b1=bmb1.move_bomb(screen)
        b2=bmb2.move_bomb(screen)
        b3=bmb3.move_bomb(screen)
        b4=bmb4.move_bomb(screen)
        b5=bmb5.move_bomb(screen)
        b6=bmb6.move_bomb(screen)


        if b1==-1:
            bmb1.remove_onscreen(screen)
            bmb1 = bomb.bomb(bos._x+2,bos._y,-1,1)
        if b2==-1:
            bmb2.remove_onscreen(screen)
            bmb2 = bomb.bomb(bos._x+10,bos._y,-1,1)
        if b3==-1:
            bmb3.remove_onscreen(screen)
            bmb3 = bomb.bomb(bos._x+4,bos._y,-1,1)
        if b4==-1:
            bmb4.remove_onscreen(screen)
            bmb4 = bomb.bomb(bos._x+8,bos._y,-1,1)
        if b5==-1:
            bmb5.remove_onscreen(screen)
            bmb5 = bomb.bomb(bos._x+6,bos._y,-1,1)
        if b6==-1:
            bmb6.remove_onscreen(screen)
            bmb6 = bomb.bomb(bos._x+12,bos._y,-1,1)

        if b1==1:
            bmb1.remove_onscreen(screen)
            bmb1 = bomb.bomb(bos._x+2,bos._y,-1,1)
            paddles.remove_onscreen(screen)
            balls.remove_onscreen(screen)
            paddles=paddle.paddle(25,48,1,5,[["="]*5])
            lf=balls._life-1
            grab=1
            balls = ball.ball(25,47,lf,1)
        if b2==1:
            bmb2.remove_onscreen(screen)
            bmb2 = bomb.bomb(bos._x+10,bos._y,-1,1)
            paddles.remove_onscreen(screen)
            balls.remove_onscreen(screen)
            paddles=paddle.paddle(25,48,1,5,[["="]*5])
            lf=balls._life-1
            grab=1
            balls = ball.ball(25,47,lf,1)
        
        if b3==1:
            bmb3.remove_onscreen(screen)
            bmb3 = bomb.bomb(bos._x+4,bos._y,-1,1)
            paddles.remove_onscreen(screen)
            balls.remove_onscreen(screen)
            paddles=paddle.paddle(25,48,1,5,[["="]*5])
            lf=balls._life-1
            grab=1
            balls = ball.ball(25,47,lf,1)
        if b4==1:
            bmb4.remove_onscreen(screen)
            bmb4 = bomb.bomb(bos._x+8,bos._y,-1,1)
            paddles.remove_onscreen(screen)
            balls.remove_onscreen(screen)
            paddles=paddle.paddle(25,48,1,5,[["="]*5])
            lf=balls._life-1
            grab=1
            balls = ball.ball(25,47,lf,1)
        if b5==1:
            bmb5.remove_onscreen(screen)
            bmb5 = bomb.bomb(bos._x+6,bos._y,-1,1)
            paddles.remove_onscreen(screen)
            balls.remove_onscreen(screen)
            paddles=paddle.paddle(25,48,1,5,[["="]*5])
            lf=balls._life-1
            grab=1
            balls = ball.ball(25,47,lf,1)
        if b6==1:
            bmb6.remove_onscreen(screen)
            bmb6 = bomb.bomb(bos._x+12,bos._y,-1,1)
            paddles.remove_onscreen(screen)
            balls.remove_onscreen(screen)
            paddles=paddle.paddle(25,48,1,5,[["="]*5])
            lf=balls._life-1
            grab=1
            balls = ball.ball(25,47,lf,1)

        time+=1
        sleep(1/30)
        if blevel==0:
            balls.remove_onscreen(screen)
            global_stuff.onpaddle=1
            # balls = setup.balls
            blevel=1
            # screen=setup.board
            for i in range(41):
                bricks[i].remove_onscreen(screen)
                pp[i].spawned=0

        bos.print_onscreen(screen)

        if grab == 1 :
            st = inp.input_to(getch)
            if st==" ":
                grab=0
                global_stuff.onpaddle=0
                paddles.move_paddle(screen, st)
                pad_pos=paddles.returnxy()
                balls.remove_onscreen(screen)
                cur_dmg = balls.retdmg()
                if global_stuff.onpaddle==1:
                   balls = ball.ball(pad_pos[0]+1,pad_pos[1]-1,lf,cur_dmg)
            
        
        a = inp.input_to(getch)
     
        bos.move_onscreen(screen,a)
        paddles.move_paddle(screen,a)
        
        ch=balls.move_ball(screen)
        if isinstance(ch,int):
            if ch==-1:
                paddles.remove_onscreen(screen)
                paddles=paddle.paddle(25,48,1,5,[["="]*5])
                lf=balls._life
                grab=1
                balls = ball.ball(25,47,lf,1)
            if ch==1:
                bos.life-=1
                os.system("aplay ./sounds/1.wav &")

                if bos.life==0:
                    system('clear')
                    print("YOU WIN")
                    exit()
        
        for x in screen:
            for el in x:
                if el == '=':
                    print(Back.RED, " ", end="")
                elif el == '1':
                    print(Back.GREEN, " ", end="")
                elif el == '2':
                    print(Back.YELLOW, " ", end="")
                elif el == '3':
                    print(Back.MAGENTA, " ", end="")
                elif el == '4':
                    print(Back.LIGHTWHITE_EX," ", end="")
                elif el == '!':
                    print(Back.LIGHTYELLOW_EX," ",end="")
                elif el == 'A':
                    print(Back.LIGHTRED_EX, " ",end="")
                else:
                    print(Back.BLACK  ,el, end="")
            print()
            balls.print_onscreen(screen)

        
        print("Life", balls._life,
            "Time played", int(time/15)
        )
        print(
            "Big Paddle", int(power_duration[0]/15),
            "Small Paddle", int(power_duration[1]/15), 
            "fast-ball", int(power_duration[2]/15),
            "thru-ball", int(power_duration[3]/15), 
            "grab-ball", int(power_duration[4]/15),
            "Shoot-paddle", int(power_duration[5]/15)
        )
        print("BOSS LEVEL")
        print("BOSS LIFE : ", end="")

        for i in range(bos.life):
            print(Back.LIGHTBLUE_EX+" ",end="")
        
        continue




    print("Life", balls._life,
        "Score", score,
        "Time played", int(time/15)
        )
    print(
        "Big Paddle", int(power_duration[0]/15),
        "Small Paddle", int(power_duration[1]/15), 
        "fast-ball", int(power_duration[2]/15),
        "thru-ball", int(power_duration[3]/15), 
        "grab-ball", int(power_duration[4]/15),
        "Shoot-paddle", int(power_duration[5]/15)
    )

    time+=1
    safeT+=1
    if safeT/600>=0 and time%600==599:
        
        for i in range(41):
            bricks[i].remove_onscreen(screen)
            bricks[i].fall(screen)
            pp[i].fall(screen)
            pppos[i]=(pppos[i][0]+1,pppos[i][1])
            pos[i]=(pos[i][0]+1,pos[i][1])
            if global_stuff.level==1:
                setup.bricks1[i].fall(screen)
                setup.pp1[i].fall(screen)
                global_stuff.pos1[i]=(pos[i][0],pos[i][1])
                global_stuff.pppos1[i]=(pppos[i][0],pppos[i][1])

            if global_stuff.level==2:
                setup.bricks2[i].fall(screen)
                setup.pp2[i].fall(screen)
                global_stuff.pos2[i]=(pos[i][0],pos[i][1])
                global_stuff.pppos2[i]=(pppos[i][0],pppos[i][1])


            
        
    for i in range(30):
        if rain_brick[i]==0:
            br_pos=bricks[i].ret_pos()
            bricks[i]=brick.brick(br_pos[0],br_pos[1],1,3,[[0]*3],random.randint(1,4))
    for i in range(41):
        bricks[i].print_onscreen(screen)

    

    if power_duration[4]>0:
        grab=1

    if grab == 1 :
        st = inp.input_to(getch)
        if st==" ":
            grab=0
            global_stuff.onpaddle=0
        paddles.move_paddle(screen, st)
        pad_pos=paddles.returnxy()
        balls.remove_onscreen(screen)
        cur_dmg = balls.retdmg()
        if global_stuff.onpaddle==1:
           balls = ball.ball(pad_pos[0]+1,pad_pos[1]-1,lf,cur_dmg)
        
    sleep(1/30)

    for i in range(6):
        if power_duration[i]>0:
            power_duration[i]-=1
            if power_duration[i] == 0:
                if i == 0:
                    pad_pos=paddles.returnxy()
                    paddles.remove_onscreen(screen)
                    paddles=paddle.paddle(pad_pos[0],pad_pos[1],1,5,[["="]*5])
                if i==1:
                    pad_pos=paddles.returnxy()
                    paddles.remove_onscreen(screen)
                    paddles=paddle.paddle(pad_pos[0],pad_pos[1],1,5,[["="]*5])
                if i == 2:
                    balls.increasexv(-2)
                if i == 3:
                    balls.increasedmg(1)
                if i == 4:
                    grab=0
                if i == 5:
                    pad_pos=paddles.returnxy()
                    paddles.remove_onscreen(screen)
                    paddles=paddle.paddle(pad_pos[0],pad_pos[1],1,5,[["="]*5])
                    bullets.remove_onscreen(screen)

    a = inp.input_to(getch)
    ch=balls.move_ball(screen)

    
    if a =='k':
        if score < 1800:
            score=1800
        if score >=3800:
            global_stuff.level=3
        if score > 1800:
            score=3800

    if isinstance(ch,int):
        if ch==-1:

            grab=1
            paddles.remove_onscreen(screen)
            bullets.remove_onscreen(screen)
            

            paddles=paddle.paddle(25,48,1,5,[["="]*5])
            lf=balls._life
            balls = ball.ball(25,47,lf,1)
            for i in range(41):
                pp[i].spawned=0
                pp[i].remove_onscreen(screen)

        else  :
            
            cur_str=bricks[ch].ret_str()
            cur_pos=bricks[ch].ret_pos()
            if ch in range(30):
                rain_brick[ch]=1
            if cur_str - balls._dmg >0:
                bricks[ch]=brick.brick(cur_pos[0],cur_pos[1],1,3,[[0]*3],cur_str-balls._dmg)


            else :
                bricks[ch]=brick.brick(cur_pos[0],cur_pos[1],1,3,[[0]*3],0)
                score+=50
                if (cur_pos[1],cur_pos[0]) in pppos:
                    pp[pppos.index((cur_pos[1],cur_pos[0]))].spawned = 1
                    os.system("aplay ./sounds/1.wav &")
                    pp[pppos.index((cur_pos[1],cur_pos[0]))]._xv = balls._xv
                    pp[pppos.index((cur_pos[1],cur_pos[0]))]._yv = balls._yv


    paddles.move_paddle(screen, a)
    balls.print_onscreen(screen)

    if power_duration[5]>0:
        
        if fire==1:
            bullets=bullet.bullet(paddles.returnxy()[0],paddles.returnxy()[1],1,1)
            fire=0
        ch=bullets.move_bullet(screen)

        if isinstance(ch,int):
            if ch==-1:
                bullets.remove_onscreen(screen)
                bullets=bullet.bullet(paddles.returnxy()[0],paddles.returnxy()[1],1,1)
            else  :

                cur_str=bricks[ch].ret_str()
                cur_pos=bricks[ch].ret_pos()
                if ch in range(30):
                    rain_brick[ch]=1
                if cur_str - balls._dmg >0:
                    bricks[ch]=brick.brick(cur_pos[0],cur_pos[1],1,3,[[0]*3],cur_str-balls._dmg)
                else :
                    bricks[ch]=brick.brick(cur_pos[0],cur_pos[1],1,3,[[0]*3],0)
                    score+=50
                    if (cur_pos[1],cur_pos[0]) in pppos:
                        pp[pppos.index((cur_pos[1],cur_pos[0]))].spawned = 1
                        os.system("aplay ./sounds/1.wav &")
                        pp[pppos.index((cur_pos[1],cur_pos[0]))]._xv = balls._xv
                        pp[pppos.index((cur_pos[1],cur_pos[0]))]._yv = balls._yv

                bullets.remove_onscreen(screen)
                bullets=bullet.bullet(paddles.returnxy()[0]+2,paddles.returnxy()[1],1,1)
            
    
    flag=0
    for i in range(41):
        if pp[i].spawned == 1:
            pp[i].print_onscreen(screen)
            flag=pp[i].move_powerup(screen) 
            if flag==1:
                pad_pos=paddles.returnxy()
                paddles.remove_onscreen(screen)
                paddles=paddle.paddle(pad_pos[0],pad_pos[1],1,10,[["="]*10])
                

            if flag==2:
                pad_pos=paddles.returnxy()
                paddles.remove_onscreen(screen)
                paddles=paddle.paddle(pad_pos[0],pad_pos[1],1,3,[["="]*3])

            if flag==3:
                balls.increasexv(2)

            if flag==4:
                balls.increasedmg(1000)

            if flag==5:
                grab=1
            if flag==6:
                fire=1
                bullets.remove_onscreen(screen)
                pad_pos=paddles.returnxy()
                paddles.remove_onscreen(screen)
                paddles=paddle.paddle(pad_pos[0],pad_pos[1],1,5,[["=","=","!","=","="]])

    for x in screen:
        for el in x:
            if el == '=':
                print(Back.RED, " ", end="")
            elif el == '1':
                print(Back.GREEN, " ", end="")
            elif el == '2':
                print(Back.YELLOW, " ", end="")
            elif el == '3':
                print(Back.MAGENTA, " ", end="")
            elif el == '4':
                print(Back.LIGHTWHITE_EX, " ", end="")
            elif el == '!':
                print(Back.LIGHTYELLOW_EX," ",end="")
            elif el == 'A':
                print(Back.LIGHTRED_EX+" ",end="")
            else:
                print(Back.BLACK ,el, end="")
            if el == bimg:
                print(Fore.LIGHTYELLOW_EX, end="")

        print()

    for el in screen[48]:
        if el=='1' or el=='2' or el=='3' or el=='4':
            print("TIME UP")
            exit()

    if score == 1800 :
        score+=200
        global_stuff.level=2

        for i in range(41):
            bricks[i].remove_onscreen(screen)
            pp[i].spawned=0
        bricks = setup.bricks2
        pp = setup.pp2
        pppos = setup.pppos2
        pos = setup.pos2
        bullets.remove_onscreen(screen)
        balls.remove_onscreen(screen)
        paddles.remove_onscreen(screen)
        balls = setup.balls
        paddles = setup.paddle
        grab=1
        safeT=0
        for i in range(len(power_duration)):
            global_stuff.power_duration[i]=0
        for i in range(30):
            rain_brick[i]=0

    if score == 3600:
        score+=200
        global_stuff.level=3

    if score==5000:
        system('clear')
        print("YOU WINN")
        exit()

    
