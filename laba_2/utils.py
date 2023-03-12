import math
import matplotlib.pyplot as plt

import config

def init():
    tmpX=[]
    tmpY=[]
    for i in range (0,len(config.DEFAULTPOINTX)):
        tmpX.append(config.DEFAULTPOINTX[i])
        tmpY.append(config.DEFAULTPOINTY[i])
    return [tmpX,tmpY]

def Print(X,Y):
    plt.close('all')
    fig, ax = plt.subplots(figsize = (10, 10))
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid()
    ax.plot(X,Y, c='r')
    plt.show(block=False)

def menu():
    print('1. Перенос вдоль оси OX')
    print('2. Перенос вдоль оси OY')
    print('3. Отражение относительно оси OX')
    print('4. Отражение относительно оси OY')
    print('5. Отражение относительно прямой Y=X')
    print('6. Масштабирование независимо по обеим осям')
    print('7. Поворот на заданный угол относительно центра координат')
    print('8. Поворот на заданный угол относительно произвольной точки, указываемой в ходе выполнения программы')
    print('9. Восстановление исходной позиции фигур')
    print('10. Выход')

def TransferX(x,a):
    return x+a

def TransferY(y,a):
    return y+a

def ShowX(y):
    return(-y)

def ShowY(x):
    return(-x)

def ShowXY(x,y):
    return [y,x]

def Scaling(z,a):
    return z*a

def TurnCentre(x,y,theta):
   theta=math.radians(theta)
   return [x*math.cos(theta)-y*math.sin(theta), x*math.sin(theta)+y*math.cos(theta)]

def TurnPoint (x,y,theta,x1,y1):
    theta=math.radians(theta)
    return [(x - x1) * math.cos(theta) - (y - y1) * math.sin(theta) + 1*x1, (x - x1) * math.sin(theta) + (y - y1) * math.cos(theta) + y1]
