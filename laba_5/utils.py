
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

def PixelFill(x,y,fx,fy,rx,ry,fillx,filly,camera,ax):
    if inFill(x,y,fillx,filly):
        return
    fillx.append(x)
    filly.append(y)
    ax.plot(fx,fy,c='blue')
    ax.scatter(rx,ry,c='red')
    ax.scatter(fillx,filly,c='red')
    camera.snap()
    xl=x-1
    while not inFill(xl,y,rx,ry):
        fillx.append(xl)
        filly.append(y)
        ax.plot(fx,fy,c='blue')
        ax.scatter(rx,ry,c='red')
        ax.scatter(fillx,filly,c='red')
        camera.snap()
        xl-=1
    xr=x+1
    while not inFill(xr,y,rx,ry):
        fillx.append(xr)
        filly.append(y)
        ax.plot(fx,fy,c='blue')
        ax.scatter(rx,ry,c='red')
        ax.scatter(fillx,filly,c='red')
        camera.snap()
        xr+=1
    ax.plot(fx,fy,c='blue')
    ax.scatter(rx,ry,c='red')
    ax.scatter(fillx,filly,c='red')
    camera.snap()
    for i in range(xl+1,xr):
        if not inFill(i,y+1,rx,ry):
            PixelFill(i,y+1,fx,fy,rx,ry,fillx,filly,camera,ax)
        if not inFill(i,y-1,rx,ry):
            PixelFill(i,y-1,fx,fy,rx,ry,fillx,filly,camera,ax)
    return fillx,filly


def inFill(x,y,fillx,filly):
    for i in range(0,len(fillx)):
        if fillx[i]==x and filly[i]==y:
            print('Выход =)')
            return True
    return False
    