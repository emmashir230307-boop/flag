import pygame
import time
import consts

state=[consts.RUNNING_STATE]

def main(state):
    if state[0]==consts.RUNNING_STATE:
        pass #print screen
    elif state[0]==consts.WIN_STATE:
        pass #print win
    elif state[0]==consts.LOSE_STATE:
        pass #print lose
    elif state[0]==consts.EXPOSE_MINES_STATE:
        #print mine screen
        time.sleep(1)
        state[0]=consts.RUNNING_STATE



if __name__=="__main__":
    main(state)