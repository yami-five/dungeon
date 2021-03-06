import curses
import os
import time
from random import randint
from map_generator import generate_map 

def draw_level(playerPos,lvlArray):
    pad=curses.newpad(20,21)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_MAGENTA)
    curses.init_pair(3,curses.COLOR_BLUE,curses.COLOR_BLUE)
    for x in range(0,20):
        for y in range(0,20):
            if lvlArray[x][y]==1:
                pad.addstr(x,y,'#',curses.color_pair(1))
            elif lvlArray[x][y]==2:
                pad.addstr(x,y,'#',curses.color_pair(2))
            elif lvlArray[x][y]==3:
                pad.addstr(x,y,'#',curses.color_pair(3))
    #pad.addstr(playerPos[0],playerPos[1],'@')
    pad.refresh(0,0,0,0,19,20)
def change_pos(key,playerPos,lvlArray):
    #Up
    if key==259:
        playerPos[0]-=1
        if playerPos[0]<0:
            playerPos[0]=0
        elif lvlArray[playerPos[0]][playerPos[1]]==1:
            playerPos[0]+=1
    #Down
    if key==258:
        playerPos[0]+=1
        if playerPos[0]>19:
            playerPos[0]=19
        elif lvlArray[playerPos[0]][playerPos[1]]==1:
            playerPos[0]-=1
    #Left
    if key==260:
        playerPos[1]-=1
        if playerPos[1]<0:
            playerPos[1]=0
        elif lvlArray[playerPos[0]][playerPos[1]]==1:
            playerPos[1]+=1
    #Right
    if key==261:
        playerPos[1]+=1
        if playerPos[1]>19:
            playerPos[1]=19
        elif lvlArray[playerPos[0]][playerPos[1]]==1:
            playerPos[1]-=1
    draw_level(playerPos,lvlArray)
    return playerPos



def main():
    lvlArray=generate_map()
    playerPos=[1,1]
    draw_level(playerPos,lvlArray)
    while True:
        key=stdscr.getch()
        if key==27:
            break


    #Up 258 Down 259 Left 260 Right 261
        # if key in range(258,262):
        #     playerPos=change_pos(key,playerPos,lvlArray)

if __name__=='__main__':
    os.system("mode con cols=20 lines=21")
    stdscr=curses.initscr()
    curses.start_color()
    stdscr.refresh()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    main()
    curses.nocbreak()
    stdscr.keypad(False)
    curses.endwin()
