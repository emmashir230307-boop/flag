import random
from random import randrange
import pygame
import consts
import solider

screen = pygame.display.set_mode((consts.SCREEN_WIDTH,consts.SCREEN_HEIGHT))
def setting_up():
    pygame.init()
    pygame.display.set_caption('Flag Game')
    draw_screen()

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
    pygame.display.flip()

def draw_matrix(lst):
    screen=pygame.display.set_mode((consts.SCREEN_WIDTH,consts.SCREEN_HEIGHT))
    screen.blit(consts.GRID_IMG,(0,0))
    for tpl in lst:
        mine_loc=(tpl[0]*consts.SQUARE,tpl[1]*consts.SQUARE)
        screen.blit(consts.MINE_IMG,mine_loc)
    pygame.display.update()

def starting_screen():
    screen.blit(consts.SOLDIER_IMG,(0,0))
    screen.blit(consts.FLAG_IMG,(consts.FLAG_POS[0]*consts.SQUARE,consts.FLAG_POS[1]*consts.SQUARE))
    pygame.display.update()

def draw_items(board): #have to call apart from other functions bc is changeable
    row=solider.all_soldier_func(board)['Row']
    col=solider.all_soldier_func(board)['Col']
    location=(row*consts.SQUARE,col*consts.SQUARE)
    screen.blit(consts.SOLDIER_IMG,location)
    pygame.display.update()

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

def draw_game(state):
    pass