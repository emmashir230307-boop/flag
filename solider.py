import consts

def make_soldier(row,col):
    soldier={'Image':consts.SOLDIER_IMG,
             'Row': row,
             'Col':col}
    return soldier

def legs_location(r,c):
    soldier_row = make_soldier(r, c)['Row']+3
    soldier_col = make_soldier(r, c)['Col']
    legs_loc_list=[(soldier_row,soldier_col),(soldier_row,soldier_col+1)]
    return legs_loc_list

def body_location(r,c):
    soldier_row=make_soldier(r,c)['Row']
    soldier_col=make_soldier(r,c)['Col']
    body_loc_lst=[]
    for i in range(consts.SOLDIER_SIZE[1]):
        for k in range(consts.SOLDIER_SIZE[0]):
            loc_tpl=(soldier_row+k,soldier_col+i)
            body_loc_lst.append(loc_tpl)
    return body_loc_lst

def out_of_range(r,c):
    if r>24 or r<0 or c<0 or c>49:
        return False
    else: return True
