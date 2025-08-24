import random
from random import randrange

import pygame
import consts

def setting_up():
    pygame.init()
    pygame.display.set_caption('Flag Game')
    draw_screen()

def draw_screen():
    screen = pygame.display.set_mode((consts.SCREEN_WIDTH,consts.SCREEN_HEIGHT))
    screen.fill(consts.SCREEN_COLOR)
    draw_grass(screen)
    pygame.display.update()

def draw_grass(screen):
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
    pygame.display.flip()

def draw_matrix(matrix):
    screen=pygame.display.set_mode((consts.SCREEN_WIDTH,consts.SCREEN_HEIGHT))
    screen.blit(consts.GRID_IMG,(0,0))
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col]==consts.MINE:
                for k in range(1,3):
                    if matrix[row][col+k]==consts.MINE:
                        continue
                    else:break
                mine_loc=(row*consts.SQUARE,col*consts.SQUARE)
                screen.blit(consts.MINE_IMG,mine_loc)
    pygame.display.update()

def draw_items(screen):
