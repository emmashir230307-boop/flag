import pygame
import time
import consts
import screen

state=[consts.RUNNING_STATE]

def main(state):
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        elif state[0]==consts.RUNNING_STATE:
            screen.setting_up()
            screen.draw_screen()
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