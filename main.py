import pygame
import time
import consts
import screen
import game_field
import solider

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

def soldier_location(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==consts.SOLDIER:
                return i,j
    return None



def up(board):
    row,col=soldier_location(board)
    if solider.out_of_range(row-1,col):
        new_row,new_col=row-1,col
        for i in range(row,row+4):
            for j in range(col,col+2):
                board[i][j] = consts.SOLDIER
        for i in range(new_row,new_row+4):
            for j in range(new_col,new_col+2):
                board[i][j] = consts.SOLDIER



if __name__=="__main__":
    main()

