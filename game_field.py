import consts
import random

board=[]

def create_board(board):
    for i in range(consts.SCREEN_SIZE[1]):
        temp=[]
        for j in range(consts.SCREEN_SIZE[0]):
            temp.append(consts.EMPTY)
        board.append(temp)
    for i in range(4):
        for j in range(2):
            board[i][j]=consts.SOLDIER
    for i in range(consts.SCREEN_SIZE[1]-3,consts.SCREEN_SIZE[1]):
        for j in range(consts.SCREEN_SIZE[0]-4,consts.SCREEN_SIZE[0]):
            board[i][j]=consts.FLAG

def insert_mines(board):
    for i in range(consts.MINE_NUM):
        row=random.randint(0,consts.SCREEN_SIZE[1]-1)
        col=random.randint(0,consts.SCREEN_SIZE[0]-3)
        while consts.MINE in board[row][col:col+3] or consts.SOLDIER in board[row][col:col+3] or consts.FLAG in board[row][col:col+3]:
            row = random.randint(0, consts.SCREEN_SIZE[1] - 1)
            col = random.randint(0, consts.SCREEN_SIZE[0] - 3)
        print(row,col)
        board[row][col:col + 3] = [consts.MINE,consts.MINE,consts.MINE]

