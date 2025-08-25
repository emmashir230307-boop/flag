
import pygame

FPS=60
SCREEN_SIZE=(50,25)
SCREEN_COLOR=(0,153,0)
SQUARE=25
SCREEN_WIDTH,SCREEN_HEIGHT = SCREEN_SIZE[0]*SQUARE,SCREEN_SIZE[1]*SQUARE
SOLDIER_SIZE=(2,4)
#1250,625
EXPLOSION_IMG='pictures/explotion.png'
EXPLOSION_IMG=pygame.image.load(EXPLOSION_IMG)
EXPLOSION_IMG=pygame.transform.scale(EXPLOSION_IMG,(3*SQUARE,1*SQUARE))

FLAG_IMG='pictures/flag.png'
FLAG_IMG=pygame.image.load(FLAG_IMG)
FLAG_IMG=pygame.transform.scale(FLAG_IMG,(4*SQUARE,3*SQUARE))

GRASS_IMG='pictures/grass.png'
GRASS_IMG=pygame.image.load(GRASS_IMG)
GRASS_IMG=pygame.transform.scale(GRASS_IMG,(SQUARE,SQUARE))

INJURY_IMG='pictures/injury.png'
INJURY_IMG=pygame.image.load(INJURY_IMG)
INJURY_IMG=pygame.transform.scale(INJURY_IMG,(2*SQUARE,4*SQUARE))

MINE_IMG='pictures/mine.png'
MINE_IMG=pygame.image.load(MINE_IMG)
MINE_IMG=pygame.transform.scale(MINE_IMG,(3*SQUARE,1*SQUARE))

SNAKE_IMG='pictures/snake.png'
SNAKE_IMG=pygame.image.load(SNAKE_IMG)
SNAKE_IMG=pygame.transform.scale(SNAKE_IMG,(3*SQUARE,3*SQUARE))

SOLDIER_IMG='pictures/soldier.png'
SOLDIER_IMG=pygame.image.load(SOLDIER_IMG)
SOLDIER_IMG=pygame.transform.scale(SOLDIER_IMG,(3*SQUARE,3*SQUARE))

SOLDIER2_IMG='pictures/soldier (2).png'
SOLDIER2_IMG=pygame.image.load(SOLDIER2_IMG)
SOLDIER2_IMG=pygame.transform.scale(SOLDIER2_IMG,(2*SQUARE,4*SQUARE))

SOLDIER_NIGHT_IMG='pictures/soldier_nigth.png'
SOLDIER_NIGHT_IMG=pygame.image.load(SOLDIER_NIGHT_IMG)
SOLDIER_NIGHT_IMG=pygame.transform.scale(SOLDIER_NIGHT_IMG,(2*SQUARE,4*SQUARE))

GRID_IMG='pictures/grid.png'
GRID_IMG = pygame.image.load(GRID_IMG)
GRID_IMG = pygame.transform.scale(GRID_IMG, (SCREEN_WIDTH, SCREEN_HEIGHT))

FLAG="flag"
SOLDIER="soldier"
MINE='mine'
EMPTY="empty"

INITIAL_SOLDIER=(0,0)
FLAG_POS=(46,22)

WIN_MESSAGE="You Win!"
LOSE_MESSAGE="You Stinky Loser"
START_MESSAGE1="Welcome to the flag game!"
START_MESSAGE2="Have Fun!"
FONT_NAME="Calibri"
BLACK=(0,0,0)
FONT_SIZE=20
GRASS_NUM=20
MINE_NUM=20

RUNNING_STATE=0
WIN_STATE=1
LOSE_STATE=2
EXPOSE_MINES_STATE=3