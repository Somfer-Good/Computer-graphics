from os import system

#Классы
import point
import line
import plane

import utils

def main():
    exit = True
    while (exit):
        print('Для продожений нажмите Enter')
        input()
        system("cls")
        utils.menu()
        print('Выберете действие:', end='')
        select = int(input())
        match select:
            case 1:
                print("Введите координаты точки: ",end='')
                str = input()
                arr = str.split(' ')
                if len(arr) == 2:
                    x = float(arr[0])
                    y = float(arr[1])
                print("Введите прямую: ",end='')
                str = input()
                arr = str.split(' ')
                if len(arr) == 3:
                    a = float(arr[0])
                    b = float(arr[1])   
                    c = float(arr[2])   
                A=point.Point(x,y)
                l=line.Line(a,b,c)
                print(utils.PointOnLine(l,A))
            case 2:
                print("Введите первую точку:", end='')
                str = input()
                arr = str.split(' ')
                if len(arr) == 2:
                    x1 = float(arr[0])
                    y1 = float(arr[1])
                print("Введите вторую точку:", end='')
                str = input()
                arr = str.split(' ')
                if len(arr) == 2:
                    x2 = float(arr[0])
                    y2 = float(arr[1])
                print("Введите третью точку:", end='')
                str = input()
                arr = str.split(' ')
                if len(arr) == 2:
                    x3 = float(arr[0])
                    y3 = float(arr[1])
                A=point.Point(x1, y1)
                B=point.Point(x2, y2)
                C=point.Point(x3, y3)
                print(utils.PointOnBeam(A, B, C))
            case 3:
                print("Введите первую точку:", end='')
                str = input()
                arr = str.split(' ')
                if len(arr) == 2:
                    x1 = float(arr[0])
                    y1 = float(arr[1])
                print("Введите вторую точку:", end='')
                str = input()
                arr = str.split(' ')
                if len(arr) == 2:
                    x2 = float(arr[0])
                    y2 = float(arr[1])
                print("Введите третью точку:", end='')
                str = input()
                arr = str.split(' ')
                if len(arr) == 2:
                    x3 = float(arr[0])
                    y3 = float(arr[1])
                A=point.Point(x1, y1)
                B=point.Point(x2, y2)
                C=point.Point(x3, y3)
                print(utils.CheakBypass(A, B, C))
            case 4:
                print("Введите коэффициенты плоскости:",end='')
                str = input()
                arr = str.split(' ')
                if len(arr) == 4:
                    a = float(arr[0])
                    b = float(arr[1])   
                    c = float(arr[2])  
                    d = float(arr[3])
                P=plane.Plane(a, b, c, d)
                print("Введите координаты точки: ",end='')
                str = input()
                arr = str.split(' ')
                if len(arr) == 3:
                    x = float(arr[0])
                    y = float(arr[1])
                    z = float(arr[2])
                A=point.Point(x, y,z)
                print(utils.PointOnPlane(P, A))
            case 5: 
                exit=False

