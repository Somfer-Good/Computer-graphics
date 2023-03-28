from os import system

import matplotlib.pyplot as plt

import SutherlandCohen,SutherlandCohenData


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
                x_min=100
                x_max=-100
                y_min=100
                y_max=-100
                for i in range(0,len(SutherlandCohenData.RECTANGLE['X'])):
                    x_min=min(x_min,SutherlandCohenData.RECTANGLE['X'][i])
                    x_max=max(x_max,SutherlandCohenData.RECTANGLE['X'][i])
                    y_min=min(y_min,SutherlandCohenData.RECTANGLE['Y'][i])
                    y_max=max(y_max,SutherlandCohenData.RECTANGLE['Y'][i])
                segmentInX,segmentInY=SutherlandCohen.cohenSutherlandClip(SutherlandCohenData.SEGMENT['X'][0],SutherlandCohenData.SEGMENT['Y'][0],
                                                            SutherlandCohenData.SEGMENT['X'][1],SutherlandCohenData.SEGMENT['Y'][1],
                                                            x_min,x_max,y_min,y_max)
                utils.drawRectangleLine(SutherlandCohenData.RECTANGLE['X'],SutherlandCohenData.RECTANGLE['Y'],
                                        SutherlandCohenData.SEGMENT['X'],SutherlandCohenData.SEGMENT['Y'],
                                        segmentInX,segmentInY)
            case 2:
                return
            case 3:
                return
            case 4:
                exit=False

