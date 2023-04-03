from os import system

import chirysBack,sutherlandCohen,midPoint

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
                sutherlandCohen.SutherlandCohen()
            case 2:
                chirysBack.ChirysBack()
            case 3:
                midPoint.midPoint()
            case 4:
                exit=False

