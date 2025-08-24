import consts

def make_soldier(soldier_location):
    soldier={'Image':consts.SOLDIER_IMG,
             'Location': soldier_location}
    return soldier

def legs_location():
    pass


def body_location(location):
    soldier_location=make_soldier(location)['Location']
    row=int(soldier_location[0])
    col=int(soldier_location[1])
    init_tpl=(row,col)
    body_loc_lst=[]
    for i in range(consts.SOLDIER_SIZE[1]):
        for k in range(consts.SOLDIER_SIZE[0]):
            loc_tpl=(init_tpl[0]+k,init_tpl[1]+i)
            body_loc_lst.append(loc_tpl)