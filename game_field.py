import consts

board=[]

def create_board(board):
    for i in range(consts.SCREEN_SIZE[0]):
        temp=[]
        for j in range(consts.SCREEN_SIZE[1]):
            temp.append(consts.EMPTY)
        board.append(temp)
create_board(board)
print(board)