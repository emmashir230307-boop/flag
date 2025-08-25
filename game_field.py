import consts
import random

board=[]

def create_board():
    for i in range(consts.SCREEN_SIZE[1]):
        temp=[]
        for j in range(consts.SCREEN_SIZE[0]):
            temp.append(consts.EMPTY)
        board.append(temp)
    for i in range(4):
        for j in range(2):
            board[i][j]=consts.SOLDIER
    for i in range(consts.FLAG_POS[1],consts.SCREEN_SIZE[1]):
        for j in range(consts.FLAG_POS[0],consts.SCREEN_SIZE[0]):
            board[i][j]=consts.FLAG

def insert_mines():
    for i in range(consts.MINE_NUM):
        row=random.randint(0,consts.SCREEN_SIZE[1]-1)
        col=random.randint(0,consts.SCREEN_SIZE[0]-3)
        while consts.MINE in board[row][col:col+3] or consts.SOLDIER in board[row][col:col+3] or consts.FLAG in board[row][col:col+3]:
            row = random.randint(0, consts.SCREEN_SIZE[1] - 1)
            col = random.randint(0, consts.SCREEN_SIZE[0] - 3)
        board[row][col:col + 3] = [consts.MINE,consts.MINE,consts.MINE]

def touched_flag(body):
    for i in body:
        if board[body[i][0]][body[i][1]]==consts.FLAG:
            return True
    return False

def touched_mine(legs):
    if board[legs[0]][legs[1]]==consts.MINE:
        return True
    return False

def flag_index():
    indexes = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==consts.FLAG:
                indexes.append((i,j))
    return indexes

def mines_index():
    indexes = []
    for i in range(len(board)):
        for j in range(len(board[i])-2):
            if board[i][j]==consts.MINE:
                flag=True
                for k in range(1,3):
                    if board[i][j+k]==consts.MINE:
                        continue
                    else:
                        flag=False
                if flag:
                    indexes.append((i,j))
    return indexes
