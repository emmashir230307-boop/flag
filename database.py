import pandas as pd
import csv
import pygame
from game_field import board
#pd.read_csv() - loading the files
#if I have a lot of rows use - filename.to_string() - inside the print command

def open_csv(num): #opens a file under that name
    with open(f'{num}.csv', mode='w') as board_rows:
        csv_write=csv.writer(board_rows, delimiter=',')
        for row in board:
            csv_write.writerow(row)

def load_csv(num): #loading a file under that name, returns false if there is no file under that name
    file=pd.read_csv(f'{num}.csv')
    if file.empty:
        return False
    else: return file

def loading(event):
    #returns the file if the com was able to open one (if there are no files under that name)
    file = True
    if event.type==pygame.K_1:
        file=load_csv(1)
    elif event.type==pygame.K_2:
        file=load_csv(2)
    elif event.type==pygame.K_3:
        file=load_csv(3)
    elif event.type==pygame.K_4:
        file=load_csv(4)
    elif event.type==pygame.K_5:
        file=load_csv(5)
    elif event.type==pygame.K_6:
        file=load_csv(6)
    elif event.type==pygame.K_7:
        file=load_csv(7)
    elif event.type==pygame.K_8:
        file=load_csv(8)
    elif event.type==pygame.K_9:
        file=load_csv(9)
    return file

def opening(event): #returns true if the file can be opened
    flag=True
    while flag:
        if event.type==pygame.K_1:
            open_csv(1)
        elif event.type==pygame.K_2:
            open_csv(2)
        elif event.type==pygame.K_3:
            open_csv(3)
        elif event.type==pygame.K_4:
            open_csv(4)
        elif event.type==pygame.K_5:
            open_csv(5)
        elif event.type==pygame.K_6:
            open_csv(6)
        elif event.type==pygame.K_7:
            open_csv(7)
        elif event.type==pygame.K_8:
            open_csv(8)
        elif event.type==pygame.K_9:
            open_csv(9)
        else: flag=False
    return flag

def checking_choice(event): #checking for the num of seconds the key was held down for
    #if more then second
    opening(event)
    #if second or less
    loading(event)
