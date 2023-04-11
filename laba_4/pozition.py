INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

def code(x, y,x_min,x_max,y_min,y_max):
    code = INSIDE
    if x < x_min:      
        code = LEFT
    elif x > x_max: 
        code = RIGHT
    if y < y_min:
        code = BOTTOM
    elif y > y_max:
        code = TOP
    return code

def prov_location(mas, st, se):

    u = 0

    x1, y1 = st[0], st[1]
    x2, y2 = se[0], se[1]

    l1_list = code(mas, x1, y1)
    l2_list = code(mas, x2, y2)

    if max(l1_list) == max(l2_list) == 0:
        u = 1

    if u != 1:
        for i in range(4):
            if l1_list[i] * l2_list[i] == 1:
                u = 2
        if u != 2:
            u = 3
    return u