import pygame
import time
import consts
import screen
import game_field

state= {
    'state':consts.RUNNING_STATE,
    'exploded':False,
}

def main(state):
    pygame.init()
    game_field.create_board(game_field.board)
    game_field.insert_mines(game_field.board)
    running = True
    clock = pygame.time.Clock()
    while running:

        clock.tick(consts.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif state['state'] == consts.RUNNING_STATE:
                continue
            elif state['state'] == consts.WIN_STATE:
                pass  # print win
            elif state['state'] == consts.LOSE_STATE:
                pass  # print lose
            elif state['state'] == consts.EXPOSE_MINES_STATE:
                screen.draw_matrix(game_field.board)
                time.sleep(1)
                state['state'] = consts.RUNNING_STATE
        #print state
    pygame.quit()





if __name__=="__main__":
    main(state)

