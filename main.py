import pygame
import time
import consts
import screen
import game_field
import solider

state= {
    'state':consts.RUNNING_STATE,
    'exploded':False,
    'running':True,
    'expose':False
}

def main():
    screen.setting_up()
    screen.starting_screen()
    game_field.create_board()
    game_field.insert_mines()
    while state['running']:
        handle_events()
        for i in game_field.board:
            print(i)
        print("\n")
        if state['state'] == consts.RUNNING_STATE:
            continue
        elif state['state'] == consts.WIN_STATE:
            pass  # print win
        elif state['state'] == consts.LOSE_STATE:
            pass  # print lose
        elif state['state'] == consts.EXPOSE_MINES_STATE:
            pass
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
        info=solider.all_soldier_func(game_field.board)
        if game_field.touched_flag(info['body']):
            state['state']=consts.WIN_STATE
        if game_field.touched_mine(info['legs']):
            state['state']=consts.LOSE_STATE



def up(board):
    info = solider.all_soldier_func(board)
    row, col = info['Row'], info["Col"]
    new_row, new_col = row-1, col
    info['Row'], info["Col"] = row-1, col
    if solider.in_range(info):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == consts.SOLDIER:
                    board[i][j] = consts.EMPTY
        for i in range(new_row, new_row + 4):
            for j in range(new_col, new_col + 2):
                board[i][j] = consts.SOLDIER


def down(board):
    info = solider.all_soldier_func(board)
    row, col = info['Row'], info["Col"]
    new_row, new_col = row+1, col
    info['Row'], info["Col"] = row+1, col
    if solider.in_range(info):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == consts.SOLDIER:
                    board[i][j] = consts.EMPTY
        for i in range(new_row, new_row + 4):
            for j in range(new_col, new_col + 2):
                board[i][j] = consts.SOLDIER

def left(board):
    info = solider.all_soldier_func(board)
    row, col = info['Row'], info["Col"]
    new_row, new_col = row, col-1
    info['Row'], info["Col"] = row, col-1
    if solider.in_range(info):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == consts.SOLDIER:
                    board[i][j] = consts.EMPTY
        for i in range(new_row, new_row + 4):
            for j in range(new_col, new_col + 2):
                board[i][j] = consts.SOLDIER

def right(board):
    info=solider.all_soldier_func(board)
    row,col=info['Row'],info["Col"]
    new_row,new_col=row,col+1
    info['Row'], info["Col"]=row,col+1
    if solider.in_range(info):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==consts.SOLDIER:
                     board[i][j] = consts.EMPTY
        for i in range(new_row,new_row+4):
            for j in range(new_col,new_col+2):
                board[i][j] = consts.SOLDIER



if __name__=="__main__":
    main()