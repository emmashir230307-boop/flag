import pygame
import time
import consts

state=consts.RUNNING_STATE

def main():
    if state==consts.RUNNING_STATE:
        pass #print screen
    elif state==consts.WIN_STATE:
        pass #print win
    elif state==consts.LOSE_STATE:
        pass #print lose
    elif state==consts.EXPOSE_MINES_STATE:
        #print mine screen
        time.sleep(1)



if __name__=="__main__":
    main()