import matplotlib.pyplot as plt
from celluloid import Camera

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

def PixelFill(x,y,fillx,filly,camera,ax):
    for i in range(0,len(fillx)):
        if fillx[i]==x and filly[i]==y:
            print('в окно нахуй')
            return
    fillx.append(x)
    filly.append(y)
    ax.scatter(fillx,filly,c='red')
    camera.snap()
    PixelFill(x+1,y,fillx,filly,camera,ax)
    PixelFill(x,y+1,fillx,filly,camera,ax)
    PixelFill(x-1,y,fillx,filly,camera,ax)
    PixelFill(x,y-1,fillx,filly,camera,ax)
    return fillx,filly