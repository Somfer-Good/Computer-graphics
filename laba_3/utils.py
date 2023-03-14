import matplotlib.pyplot as plt

def ShowX(y): #1
    return(-y)

def ShowY(x): #2
    return(-x)

def ShowXY(x,y): #3
    return [y,x]

def CheckQuarter(x,y):
        if x * y > 0:
            if x > 0:  
                return 1
            else:
                return 3
        else:
            if y < 0:
                return 4
            else:
                return 2

def bresenhamLine(x1,y1,x2,y2):
    
    dx = x2 - x1
    dy = y2 - y1

    is_steep = abs(dy) > abs(dx)
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    swapped = False
    if x1>x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True
    
    dx = x2 - x1
    dy = y2 - y1

    err=int(dx/2)
    if y1<y2:
        ystep=1
    else:
        ystep=-1
    
    y=y1
    pointsX=[]
    pointsY=[]
    for x in range(x1,x2+1):
        if is_steep:
            pointsX.append(y)
            pointsY.append(x)
        else:
            pointsX.append(x)
            pointsY.append(y)
        err-=abs(dy)
        if err<0:
            y+=ystep
            err+=dx

    if swapped:
        pointsX.reverse()
        pointsY.reverse()

    return pointsX,pointsY

def graphLine(coordX,сoordY):
    plt.close('all')
    fig, ax = plt.subplots()
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid()
    ax.scatter(coordX,сoordY, c='r')
    plt.show()

def bresenhamCricle(xc,yc,r):
    сoordX=[]
    сoordY=[]
    x,y = 0,r
    d = 3 - 2 * r
    сoordX.extend([xc+x,xc-x,xc+x,xc-x,xc+y,xc-y,xc+y,xc-y])
    сoordY.extend([yc+y,yc+y,yc-y,yc-y,yc+x,yc+x,yc-x,yc-x])
    while y>=x:
        x+=1
        if d>0:
            y-=1
            d=d+4*(x-y)
        else:
            d = d + 4 * x
        сoordX.extend([xc+x,xc-x,xc+x,xc-x,xc+y,xc-y,xc+y,xc-y])
        сoordY.extend([yc+y,yc+y,yc-y,yc-y,yc+x,yc+x,yc-x,yc-x])
    return сoordX,сoordY

def graphCricle(x,y,r):
    сoordX,сoordY=bresenhamCricle(x,y,r)
    figure, ax = plt.subplots()
    plt.grid()
    Drawing_colored_circle = plt.Circle((x, y), r ,fill = False)
    ax.scatter(сoordX,сoordY, c='r')
    ax.set_aspect( 1 )
    ax.add_artist( Drawing_colored_circle )
    plt.show()

def menu():
    print('1. Отрезок')
    print('2. Окружность')
    print('3. Выход ')