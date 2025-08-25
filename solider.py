import consts

def make_soldier(soldier_location):
    soldier={'Image':consts.SOLDIER_IMG,
             'Row': soldier_location[0],
             'Col':soldier_location[1],}
    return soldier

def legs_location(soldier):
    soldier_row = soldier['Row']+3
    soldier_col = soldier['Col']
    legs_loc_list=[(soldier_row,soldier_col),(soldier_row,soldier_col+1)]
    return legs_loc_list

def body_location(soldier):
    soldier_row=soldier['Row']
    soldier_col=soldier['Col']
    body_loc_lst=[]
    for i in range(consts.SOLDIER_SIZE[1]):
        for k in range(consts.SOLDIER_SIZE[0]):
            loc_tpl=(soldier_row+k,soldier_col+i)
            body_loc_lst.append(loc_tpl)
    return body_loc_lst

def in_range(soldier):
    if soldier['Row']>24 or soldier['Row']<0 or soldier['Col']<0 or soldier['Col']>49:
        return False
    else: return True

def all_soldier_func(board):
    soldier_location=('','')
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==consts.SOLDIER:
                soldier_location=(i,j)
    soldier=make_soldier(soldier_location)
    if in_range(soldier):
        legs_indexes = legs_location(soldier)
        body_indexes = body_location(soldier)
        soldier_info={'legs':legs_indexes,'body':body_indexes,'Row':soldier_location[0],'Col':soldier_location[1]}
        return soldier_info
    else:
        return False