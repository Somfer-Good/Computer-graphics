import matplotlib.pyplot as plt
from math import *

def menu():
    print('1. Задание 1. Алгоритм Сазерленда-Коэна.')
    print('2. Задание 2. Алгоритм Цируса-Бека.')
    print('3. Задание 3. Алгоритм средней точки.')
    print('4. Выход.')

def window(mas):
    fig, ax = plt.subplots()
    plt.grid()
    plt.xlim([-20, 20])
    plt.ylim([-20, 20])

    window_x = [mas[0], mas[0], mas[2], mas[2], mas[0]]
    window_y = [mas[1], mas[3], mas[3], mas[1], mas[1]]

    plt.plot(window_x, window_y, c='black')


def visual(w, s_start, s_end, ans):

    window(w)

    x = []
    y = []

    if len(ans) > 1:
        if ans[0][0] == ans[1][0] and ans[0][1] == ans[1][1]:
            if (s_start[0] == ans[0][0] and s_start[1] == ans[0][1]) or (s_end[0] == ans[0][0] and
                                                                         s_end[1] == ans[0][1]):
                for i in range(len(ans)):
                    x.append(ans[i][0])
                    y.append(ans[i][1])
                plt.scatter(x, y, c='red', s=10)
            else:
                if w[0] <= s_start[0] <= w[2] and w[1] <= s_start[1] <= w[3]:
                    plt.plot([s_start[0], ans[0][0]], [s_start[1], ans[0][1]], color='red')
                    plt.plot([ans[0][0], s_end[0]], [ans[0][1], s_end[1]], color='blue',linestyle = 'dashed')
                else:
                    plt.plot([s_end[0], ans[0][0]], [s_end[1], ans[0][1]], color='red')
                    plt.plot([ans[0][0], s_start[0]], [ans[0][1], s_start[1]], color='blue',linestyle = 'dashed')

        else:
            s1 = sqrt((s_start[0]-ans[0][0]) ** 2 + (s_start[1] - ans[0][1]) ** 2)
            s2 = sqrt((s_start[0]-ans[1][0]) ** 2 + (s_start[1] - ans[1][1]) ** 2)
            print(s1, s2)
            if s1 < s2:
                plt.plot([s_start[0], ans[0][0]], [s_start[1], ans[0][1]], color='blue',linestyle = 'dashed')
                plt.plot([ans[0][0], ans[1][0]], [ans[0][1], ans[1][1]], color='red')
                plt.plot([ans[1][0], s_end[0]], [ans[1][1], s_end[1]], color='blue',linestyle = 'dashed')
            else:
                plt.plot([s_start[0], ans[1][0]], [s_start[1], ans[1][1]], color='blue',linestyle = 'dashed')
                plt.plot([ans[1][0], ans[0][0]], [ans[1][1], ans[0][1]], color='red')
                plt.plot([ans[0][0], s_end[0]], [ans[0][1], s_end[1]], color='blue',linestyle = 'dashed')
    else:
        if (s_start[0] == ans[0][0] and s_start[1] == ans[0][1]) or (s_end[0] == ans[0][0] and s_end[1] == ans[0][1]):
            for i in range(len(ans)):
                x.append(ans[i][0])
                y.append(ans[i][1])
            plt.scatter(x, y, c='r', s=10)
            if s_start[0] == ans[0][0] and s_start[1] == ans[0][1]:
                plt.plot([s_start[0], s_end[0]], [s_start[1], s_end[1]], color='blue',linestyle = 'dashed')
            else:
                plt.plot([s_end[0], s_start[0]], [s_end[1], s_start[1]], color='blue',linestyle = 'dashed')

        else:
            if w[0] <= s_start[0] <= w[2] and w[1] <= s_start[1] <= w[3]:
                plt.plot([s_start[0], ans[0][0]], [s_start[1], ans[0][1]], color='red')
                plt.plot([ans[0][0], s_end[0]], [ans[0][1], s_end[1]], color='blue',linestyle = 'dashed')
            else:
                plt.plot([s_end[0], ans[0][0]], [s_end[1], ans[0][1]], color='red')
                plt.plot([ans[0][0], s_start[0]], [ans[0][1], s_start[1]], color='blue',linestyle = 'dashed')




def code(arr, x, y):
    Ax = arr[0]
    Ay = arr[1]
    Bx = arr[2]
    By = arr[3]

    l_list = []

    if x < Ax:
        l_list.append(1)
    else:
        l_list.append(0)
    if y <= By:
        l_list.append(0)
    else:
        l_list.append(1)
    if y < Ay:
        l_list.append(1)
    else:
        l_list.append(0)
    if x <= Bx:
        l_list.append(0)
    else:
        l_list.append(1)

    return l_list


def provLocation(mas, st, se):

    u = 0

    x1, y1 = st[0], st[1]
    x2, y2 = se[0], se[1]

    l1_list = code(mas, x1, y1)
    l2_list = code(mas, x2, y2)

    if max(l1_list) == max(l2_list) == 0:
        u = 1

    if u != 1:
        for i in range(4):
            if l1_list[i] * l2_list[i] == 1:
                u = 2
        if u != 2:
            u = 3
    #print(u)
    return u


def provSegment(p, mas, st, se, w1):

    Ax = w1[0]
    Ay = w1[1]
    Bx = w1[2]
    By = w1[3]

    if (st[0] <= p[0] <= se[0] and Ax <= p[0] <= Bx and Ay <= p[1] <= By and st[1] <= p[1] <= se[1]) or\
            (st[0] >= p[0] >= se[0] and Ax <= p[0] <= Bx and Ay <= p[1] <= By and st[1] >= p[1] >= se[1])\
            or (st[0] <= p[0] <= se[0] and Ax <= p[0] <= Bx and Ay <= p[1] <= By and st[1] >= p[1] >= se[1])\
            or (st[0] >= p[0] >= se[0] and Ax <= p[0] <= Bx and Ay <= p[1] <= By and st[1] <= p[1] <= se[1]):
        mas.append(p)
    return mas