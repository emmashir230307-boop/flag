import pygame
import time
import consts
import screen
import game_field
import solider

state= {
    'running':True,
    'state':consts.RUNNING_STATE,
    'exploded':False,
    'expose':False
}

def main():
    screen.setting_up()
    screen.starting_screen()
    game_field.create_board()
    game_field.insert_mines()
    while state['running']:
        handle_events()

    pygame.quit()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state['running']=False
        elif state['state']!=consts.RUNNING_STATE:
            continue
        #diffrent events
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move('up')
            elif event.key==pygame.K_DOWN:
                move('down')
            elif event.key==pygame.K_RIGHT:
                move('right')
            elif event.key==pygame.K_LEFT:
                move('left')
            elif event.key==pygame.K_KP_ENTER:
                state['state']=consts.EXPOSE_MINES_STATE


def move(direction):
    info = solider.all_soldier_func(game_field.board)
    row, col = info['Row'], info["Col"]
    move_row=0
    move_col = 0
    if direction=='up':
        move_row=-1
    elif direction=='down':
        move_row=1
    elif direction=='left':
        move_col=-1
    elif direction=='right':
        move_col=1
    new_row, new_col = row+move_row, col+move_col
    info['Row'], info["Col"] = row+move_row, col+move_col
    if game_field.touched_mine(solider.legs_location(info)):
        state['state']=consts.LOSE_STATE
    elif game_field.touched_flag(solider.body_location(info)):
        state['state']=consts.WIN_STATE
    else:
        if solider.in_range(info):
            for i in range(len(game_field.board)):
                for j in range(len(game_field.board[i])):
                    if game_field.board[i][j] == consts.SOLDIER:
                        game_field.board[i][j] = consts.EMPTY
            for i in range(new_row, new_row + 4):
                for j in range(new_col, new_col + 2):
                    game_field.board[i][j] = consts.SOLDIER


if __name__=="__main__":
    main()