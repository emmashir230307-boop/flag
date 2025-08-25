import random
from random import randrange
import pygame
import consts
import solider
from game_field import board

screen = pygame.display.set_mode((consts.SCREEN_WIDTH,consts.SCREEN_HEIGHT))
def setting_up():
    pygame.init()
    pygame.display.set_caption('Flag Game')


def draw_screen():
    screen.fill(consts.SCREEN_COLOR)
    draw_grass()
    pygame.display.update()

def draw_grass():
    img=consts.GRASS_IMG
    grass_loc=[]
    screen_size=consts.SCREEN_SIZE
    row_lst=[]
    col_lst=[]
    for num in range(screen_size[0]):
        row_lst.append(num)
    for no in range(screen_size[1]):
        col_lst.append(no)
    com_choice_row=random.sample(row_lst,consts.GRASS_NUM)
    com_choice_col=random.sample(col_lst,consts.GRASS_NUM)
    for i in range(len(com_choice_row)):
        loc_tpl=(com_choice_row[i]*consts.SQUARE,com_choice_col[i]*consts.SQUARE)
        grass_loc.append(loc_tpl)
    for tpl in grass_loc:
        while tpl==consts.INITIAL_SOLDIER or tpl==consts.FLAG_POS or tpl[0]>consts.SCREEN_WIDTH or tpl[1]>consts.SCREEN_HEIGHT:
            row_choice=randrange(screen_size[0])
            col_choice=randrange(screen_size[1])
            tpl=(row_choice,col_choice)
            continue
        screen.blit(img, tpl)
    pygame.display.update()

def draw_matrix(lst):
    sc=pygame.display.set_mode((consts.SCREEN_WIDTH,consts.SCREEN_HEIGHT))
    sc.blit(consts.GRID_IMG,(0,0))
    for tpl in lst:
        mine_loc=(tpl[0]*consts.SQUARE,tpl[1]*consts.SQUARE)
        sc.blit(consts.MINE_IMG,mine_loc)
    pygame.display.flip()

def starting_screen():
    screen.blit(consts.SOLDIER_IMG,(0,0))
    draw_message(consts.START_MESSAGE1,12,(0,0,0),(3*consts.SQUARE,0))
    draw_message(consts.START_MESSAGE2, 12, (0, 0, 0), (3 * consts.SQUARE, 13))
    screen.blit(consts.FLAG_IMG,(consts.FLAG_POS[0]*consts.SQUARE,consts.FLAG_POS[1]*consts.SQUARE))
    pygame.display.update()

def draw_items(game_board): #have to call apart from other functions bc is changeable
    row=solider.all_soldier_func(game_board)['Row']
    col=solider.all_soldier_func(game_board)['Col']
    location=(row*consts.SQUARE,col*consts.SQUARE)
    screen.blit(consts.SOLDIER_IMG,location)
    pygame.display.update()

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

def draw_game(state):
    if state['state']==consts.LOSE_STATE:
        draw_message(consts.LOSE_MESSAGE,consts.FONT_SIZE,consts.BLACK,(consts.SCREEN_WIDTH,consts.SCREEN_HEIGHT/2))
        pygame.time.wait(10000)
    elif state['state']==consts.WIN_STATE:
        draw_message(consts.WIN_MESSAGE,consts.FONT_SIZE,consts.BLACK,(consts.SCREEN_WIDTH,consts.SCREEN_HEIGHT/2))
        pygame.time.wait(10000)
    elif state['state']==consts.EXPOSE_MINES_STATE:
        draw_matrix(board)
        pygame.time.wait(1000)