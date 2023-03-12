from os import system

import utils

def main():
    X,Y=utils.init()
    exit = True
    while (exit):
        utils.Print(X,Y)
        print('Для продожений нажмите Enter')
        input()
        system("cls")
        utils.menu()
        print('Выберете действие:', end='')
        select = int(input())
        match select:
            case 1:
                print('На сколько перносим:', end='')
                a=float(input())
                for i in range(0,len(X)):
                    X[i]=utils.TransferX(X[i],a)
            case 2:
                print('На сколько перносим:', end='')
                a=float(input())
                for i in range(0,len(Y)):
                    Y[i]=utils.TransferX(Y[i],a)
            case 3:
                for i in range(0,len(Y)):
                    Y[i]=utils.ShowX(Y[i])
            case 4:
                for i in range(0,len(X)):
                    X[i]=utils.ShowY(X[i])
            case 5:
                for i in range(0,len(X)):
                    X[i],Y[i]=utils.ShowXY(X[i],Y[i])
            case 6:
                print('На сколько масштабируем:', end='')
                a=float(input())
                print('1. по X')
                print('2. по Y')
                selectdop = int(input())
                if selectdop==1:
                    for i in range(0,len(X)):
                        X[i]=utils.Scaling(X[i],a)
                else:
                    for i in range(0,len(Y)):
                        Y[i]=utils.Scaling(Y[i],a)
            case 7:
                print('Введите угол:',end='')
                ang=int(input())
                for i in range(0,len(X)):
                    X[i],Y[i]=utils.TurnCentre(X[i],Y[i],ang)
            case 8:
                print('Введите угол:',end='')
                ang=int(input())
                print('Введите точку:',end='')
                str = input()
                arr = str.split(' ')
                if len(arr) == 2:
                    x = float(arr[0])
                    y = float(arr[1])
                for i in range(0,len(X)):
                    X[i],Y[i]=utils.TurnPoint(X[i],Y[i],ang,x,y)
            case 9:
                X,Y=utils.init()
            case 10:
                exit=False
            
            