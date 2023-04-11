import matplotlib.pyplot as plt
from celluloid import Camera

import utils

import data

def main():
    fig, ax = plt.subplots()
    camera = Camera(fig)
    plt.grid()

    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    f=data.FIGURA
    fx,fy=[],[]
    f=f.split(' ')
    for i in range(0,len(f),2):
        fx.append(int(f[i]))
        fy.append(int(f[i+1]))
    fx.append(int(fx[0]))
    fy.append(int(fy[0]))
    rx,ry=[],[]
    for i in range(0,len(fx)-1):
        tmpX,tmpY=utils.bresenhamLine(fx[i],fy[i],fx[i+1],fy[i+1])
        tmpX.pop()
        tmpY.pop()
        for j in range(0,len(tmpX)):
            rx.append(tmpX[j])
            ry.append(tmpY[j])
    camera.snap()
    zx,zy=data.ZATRAVKA
    rx,ry=utils.PixelFill(zx,zy,rx,ry,camera,ax)
    camera.snap()
    ax.scatter(rx,ry,c='red')
    ax.plot(fx,fy,c='blue')
    camera.snap()
    animation = camera.animate()
    animation.save('algos.gif')