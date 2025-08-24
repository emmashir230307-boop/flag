import pygame

FPS=60
SCREEN_SIZE=(25,50)
SCREEN_COLOR=(0,153,0)
SQUARE=50
SCREEN_WIDTH,SCREEN_HEIGHT = SCREEN_SIZE[0]*SQUARE,SCREEN_SIZE[1]*SQUARE

EXPLOSION_IMG='picture/explotion.png'
EXPLOSION_IMG=pygame.image.load(EXPLOSION_IMG)
EXPLOSION_IMG=pygame.transform.scale(EXPLOSION_IMG,(3*SCREEN_WIDTH,1*SCREEN_HEIGHT))

FLAG_IMG='pictures/flag.png'
FLAG_IMG=pygame.image.load(FLAG_IMG)
FLAG_IMG=pygame.transform.scale(FLAG_IMG,(4*SCREEN_WIDTH,3*SCREEN_HEIGHT))

GRASS_IMG='picture/grass.png'
GRASS_IMG=pygame.image.load(GRASS_IMG)
GRASS_IMG=pygame.transform.scale(GRASS_IMG,(2*SCREEN_WIDTH,2*SCREEN_HEIGHT))

INJURY_IMG='picture/injury.png'
INJURY_IMG=pygame.image.load(INJURY_IMG)
INJURY_IMG=pygame.transform.scale(INJURY_IMG,(2*SCREEN_WIDTH,4*SCREEN_HEIGHT))

MINE_IMG='picture/mine.png'
MINE_IMG=pygame.image.load(MINE_IMG)
MINE_IMG=pygame.transform.scale(MINE_IMG,(3*SCREEN_WIDTH,1*SCREEN_HEIGHT))

SNAKE_IMG='picture/snake.png'
SNAKE_IMG=pygame.image.load(SNAKE_IMG)
SNAKE_IMG=pygame.transform.scale(SNAKE_IMG,(3*SCREEN_WIDTH,3*SCREEN_HEIGHT))

SOLDIER_IMG='picture/soldier.png'
SOLDIER_IMG=pygame.image.load(SOLDIER_IMG)
SOLDIER_IMG=pygame.transform.scale(SOLDIER_IMG,(2*SCREEN_WIDTH,4*SCREEN_HEIGHT))

SOLDIER2_IMG='picture/soldier (2).png'
SOLDIER2_IMG=pygame.image.load(SOLDIER2_IMG)
SOLDIER2_IMG=pygame.transform.scale(SOLDIER2_IMG,(2*SCREEN_WIDTH,4*SCREEN_HEIGHT))

SOLDIER_NIGHT_IMG='picture/soldier_nigth.png'
SOLDIER_NIGHT_IMG=pygame.image.load(SOLDIER_NIGHT_IMG)
SOLDIER_NIGHT_IMG=pygame.transform.scale(SOLDIER_NIGHT_IMG,(2*SCREEN_WIDTH,4*SCREEN_HEIGHT))

FLAG="flag"
SOLDIER="soldier"
EMPTY="empty"
WIN_MESSAGE="You Win!"
LOSE_MESSAGE="You Stinky Loser"
START_MESSAGE="Welcome to the flag game!\nHave Fun!"
GRASS_NUM=20