import matplotlib.pyplot as plt
from random import randint
from celluloid import Camera
import math

import point

def sort(a,b):
  for i in range(0,len(a)):
    flag = True
    for j in range(0,len(a)-(i+1)):
        if a[j] > a[j + 1]:
            flag = False
            a[j],a[j+1]=a[j+1],a[j]
            b[j],b[j+1]=b[j+1],b[j]
        elif a[j] == a[j + 1]:
           if b[j] > b[j + 1]:
                flag = False
                a[j],a[j+1]=a[j+1],a[j]
                b[j],b[j+1]=b[j+1],b[j]
    if flag:
      return a,b

def area(Ax,Ay,Bx,By,Cx,Cy):
    return abs((Ax * (By - Cy) + Bx * (Cy - Ay) + Cx * (Ay - By)) / 2)


def square(Ax,Ay,Bx,By,Cx,Cy,Dx,Dy):
    q=0.001
    A = area(Ax, Ay, Bx, By, Cx, Cy)
    A1 = area(Dx, Dy, Bx, By, Cx, Cy)
    A2 = area(Ax, Ay, Dx, Dy, Cx, Cy)
    A3 = area(Ax, Ay, Bx, By, Dx, Dy)
    return A == (A1 + A2 + A3) 

def onLine(Ax,Ay,Bx,By,Cx,Cy):
    return (Cy - Ay) * (Bx - Ax) == (By - Ay) * (Cx - Ax)

def randomPoint(n):
    x=[]
    y=[]
    while(len(x)!=n):
        tmpX=randint(-10,10)    
        tmpY=randint(-10,10)    
        f=False
        for i in range(0,len(x)):
            if (tmpX==x[i]) and (tmpY==y[i]):
                f=True
                break
        if not f:
            x.append(tmpX)
            y.append(tmpY)

    return x,y

def parsStr(p):
    x=[]
    y=[]
    p=p.split(' ')
    for i in range(0,len(p),2):
        x.append(int(p[i]))
        y.append(int(p[i+1]))
    return x,y

def main():
    fig, ax = plt.subplots(figsize=(16,10), dpi= 80) 
    camera = Camera(fig)
    print('1. Рандом')
    print('2. Вручную')
    s=int(input())
    if s==1:
        n=int(input('Введите количество точек: '))
        x,y=randomPoint(n)
    if s==2:
        x,y=parsStr(point.POINT)
    n=len(x)
    xObl=[]
    yObl=[]
    Obl=[]
    flag=[1]*n
    x,y=sort(x,y)
    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
            for k in range(j+1,len(x)):
                ax.scatter(x,y,c='r')
                ax.plot([x[i],x[j]],[y[i],y[j]],c='b')
                ax.plot([x[j],x[k]],[y[j],y[k]],c='b')
                ax.plot([x[i],x[k]],[y[i],y[k]],c='b')
                camera.snap()
                for l in range(0,len(x)):
                    if l==i and l==j and l==k:
                        continue
                    if square(x[i],y[i],x[j],y[j],x[k],y[k],x[l],y[l]):
                        if not onLine(x[i],y[i],x[j],y[j],x[l],y[l]) and not onLine(x[j],y[j],x[k],y[k],x[l],y[l]) and not onLine(x[i],y[i],x[k],y[k],x[l],y[l]):
                            flag[l]=0
    for i in range(0,len(x)):
        if flag[i]==1:
            Obl.append((x[i],y[i]))
    startPoint = Obl[0]
    for p in Obl:
        if p[1] < startPoint[1] or (p[1] == startPoint[1] and p[0] < startPoint[0]):
            startPoint = p
    Obl = sorted(Obl, key=lambda p: math.atan2(p[1]-startPoint[1], p[0]-startPoint[0]))
    for i in range(0,len(Obl)):
        xObl.append(Obl[i][0])
        yObl.append(Obl[i][1])
    xObl.append(xObl[0])
    yObl.append(yObl[0])
    for i in range(0,5):
        
        ax.plot(xObl,yObl,c='purple')
        ax.scatter(x,y,c='r')
        camera.snap()
    animation = camera.animate()
    animation.save('algos.gif')
