import random
import pygame

def setting_up():
    pygame.init()
    pygame.display.set_caption('Flag Game')
    clock=pygame.time.Clock()
    running = True
    while running:
        clock.tick(consts.FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

    pygame.quit()
def draw_screen():
    screen = pygame.display.set_mode(consts.SCREEN_WIDTH,consts.SCREEN_HEIGHT)
    screen.fill(consts.SCREEN_COLOR)
    draw_grass(screen)
    pygame.display.update()

def draw_grass(screen):
    img=consts.GRASS_IMG
    grass_loc=[]
    screen_size=consts.SCREEN_SIZE
    com_choice_row=random.sample(screen_size[0],consts.GRASS_NUM)
    com_choice_col=random.sample(screen_size[1],consts.GRASS_NUM)
    for i in range(len(com_choice_row)):
        loc_tpl=(com_choice_row[i],com_choice_col[i])
        grass_loc.append(loc_tpl)
    for tpl in grass_loc:
        screen.blit(img,tpl)
    pygame.display.flip()


