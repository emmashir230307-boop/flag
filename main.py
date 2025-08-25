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
    screen.setting_up()
    board=game_field.create_board()
    screen.starting_screen()
    game_field.insert_mines()
    while state['running']:
        handle_events()
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
        #main screen func
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
                up(game_field.board)

            elif event.key==pygame.K_DOWN:
                down(game_field.board)
            elif event.key==pygame.K_RIGHT:
                right(game_field.board)
            elif event.key==pygame.K_LEFT:
                left(game_field.board)
            elif event.key==pygame.K_KP_ENTER:
                state['state']=consts.EXPOSE_MINES_STATE
        #win lose


def up(board):
    row, col = solider.all_soldier_func(board)
    new_row,new_col=row-1,col
    for i in range(row,row+4):
        for j in range(col,col+2):
            board[i][j] = consts.EMPTY
    for i in range(new_row,new_row+4):
        for j in range(new_col,new_col+2):
            board[i][j] = consts.SOLDIER
    if solider.all_soldier_func(board) is False:
        pass


def down(board):
    row,col=solider.all_soldier_func(board)
    new_row,new_col=row+1,col
    for i in range(row,row+4):
        for j in range(col,col+2):
            board[i][j] = consts.EMPTY
    for i in range(new_row,new_row+4):
        for j in range(new_col,new_col+2):
            board[i][j] = consts.SOLDIER
    solider.all_soldier_func(board)
    if solider.all_soldier_func(board) is False:
        pass

def left(board):
    row,col=solider.all_soldier_func(board)
    new_row,new_col=row,col-1
    for i in range(row,row+4):
        for j in range(col,col+2):
            board[i][j] = consts.EMPTY
    for i in range(new_row,new_row+4):
        for j in range(new_col,new_col+2):
            board[i][j] = consts.SOLDIER
    solider.all_soldier_func(board)
    if solider.all_soldier_func(board) is False:
        pass

def right(board):
    row,col=solider.all_soldier_func(board)
    new_row,new_col=row,col+1
    for i in range(row,row+4):
        for j in range(col,col+2):
            board[i][j] = consts.EMPTY
    for i in range(new_row,new_row+4):
        for j in range(new_col,new_col+2):
            board[i][j] = consts.SOLDIER
    solider.all_soldier_func(board)
    if solider.all_soldier_func(board) is False:
        pass


if __name__=="__main__":
    main()