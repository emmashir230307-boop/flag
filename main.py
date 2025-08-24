import pygame
import time
import consts
import screen
import game_field

state= {
    'state':consts.RUNNING_STATE,
    'exploded':False,
    'won':False,
    'running':True
}

def main():
    pygame.init()
    game_field.create_board(game_field.board)
    game_field.insert_mines(game_field.board)
    while state['running']:

        if state['state'] == consts.RUNNING_STATE:
            continue
        elif state['state'] == consts.WIN_STATE:
            pass  # print win
        elif state['state'] == consts.LOSE_STATE:
            pass  # print lose
        elif state['state'] == consts.EXPOSE_MINES_STATE:
            screen.draw_matrix(game_field.board)
            time.sleep(1)
            state['state'] = consts.RUNNING_STATE
        screen.setting_up()
    pygame.quit()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state['running']=False
        elif state['state']!=consts.RUNNING_STATE:
            continue
        #if game_field.touched_flag(game_field.board,)



if __name__=="__main__":
    main(state)

