import pygame
import time
import consts
import screen
import game_field

state=[consts.RUNNING_STATE]

def main(state):
    pygame.init()
    game_field.create_board(game_field.board)
    game_field.insert_mines(game_field.board)
    for event in pygame.event.get():
        if state[0]==consts.RUNNING_STATE:
            screen.setting_up()
        elif state[0]==consts.WIN_STATE:
            pass #print win
        elif state[0]==consts.LOSE_STATE:
            pass #print lose
        elif state[0]==consts.EXPOSE_MINES_STATE:
            screen.draw_matrix(game_field.board)
            time.sleep(1)
            state[0]=consts.RUNNING_STATE



if __name__=="__main__":
    main(state)

running = True
clock=pygame.time.Clock()
while running:
    clock.tick(consts.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()