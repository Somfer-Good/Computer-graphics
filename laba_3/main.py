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
                x,y=int(arr[0]),int(arr[1])
                print('Введите точку конца:')
                str = input()
                arr = str.split(' ')
                x1,y1=int(arr[0]),int(arr[1])
                x1-=x
                y1-=y
                x=0
                y=0
                utils.graphLine(x,y,x1,y1)
            case 2:
                print('Введите точку центра и радиус')
                str = input()
                arr = str.split(' ')
                x,y,r=int(arr[0]),int(arr[1]),int(arr[2])
                utils.graphCricle(x,y,r)
            case 3:
                exit=False

    

           
