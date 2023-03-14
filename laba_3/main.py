from os import system

import utils

def main():
    exit = True
    while exit:
        print('Для продожений нажмите Enter')
        input()
        system("cls")
        utils.menu()
        print('Выберете действие:', end='')
        select = int(input())
        match select:
            case 1:
                print('Введите точку начала:')
                str = input()
                arr = str.split(' ')
                x1,y1=int(arr[0]),int(arr[1])
                print('Введите точку конца:')
                str = input()
                arr = str.split(' ')
                x2,y2=int(arr[0]),int(arr[1])
                pointX=[x1,x2]
                pointY=[y1,y2]
                x2-=x1
                y2-=y1
                x1=0
                y1=0
                pointsX,pointsY=utils.bresenhamLine(x1,y1,x2,y2)
                while True:
                    cq=utils.CheckQuarter(x2,y2)
                    if cq==1:
                        if x2>=y2:
                            break
                        else:
                           x2,y2=utils.ShowXY(x2,y2)
                           pointX.append(x2)
                           pointY.append(y2)
                    elif cq==2:
                        x2=utils.ShowY(x2)
                        pointX.append(x2)
                        pointY.append(y2)
                    elif cq==3:
                        x2=utils.ShowY(x2)
                        pointX.append(x2)
                        pointY.append(y2)
                    elif cq==4:
                        y2=utils.ShowX(y2)
                        pointX.append(x2)
                        pointY.append(y2)
                    pointX.append(0)
                    pointY.append(0)
                
                #print(pointX)
                for i in range(0,len(pointX),2):
                    p1,p2=utils.bresenhamLine(pointX[i],pointY[i],pointX[i+1],pointY[i+1])
                    #print(p1)
                    for j in range(0,len(p1)):
                        pointsX.append(p1[j])
                        pointsY.append(p2[j])
                utils.graphLine(pointsX,pointsY)
            case 2:
                print('Введите точку центра и радиус')
                str = input()
                arr = str.split(' ')
                x,y,r=int(arr[0]),int(arr[1]),int(arr[2])
                utils.graphCricle(x,y,r)
            case 3:
                exit=False

    

