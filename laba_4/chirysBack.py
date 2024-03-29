import numpy as np
import matplotlib.pyplot as plt

def ChirysBack():
    fig, ax = plt.subplots()
    plt.grid()
    plt.xlim(-20,20)
    plt.ylim(-20,20)
    print('Количество вершин:')
    n = int(input())
    print("Фигура:")
    w = [float(i) for i in input().split()]
    print("Начало отрезка:")
    s_start = [float(i) for i in input().split()]
    print("Конец отрезка:")
    s_end = [float(i) for i in input().split()]
    w.append(w[0])
    w.append(w[1])
    w = np.array(w)
    w = w.reshape(n + 1, 2)

    xo, yo, xn, yn = 0, 0, 0, 0
    vis = 1
    t0, t1 = 0, 1
    p = [s_end[0] - s_start[0], s_end[1] - s_start[1]]

    mx, my = [], []
    for i in range(len(w)):
        mx.append(w[i][0])
        my.append(w[i][1])
    #mx.append(w[0][0])
    #my.append(w[0][1])
    plt.plot(mx, my)

    for i in range(n):
        f = w[i]
        q = np.array([s_start[0] - f[0], s_start[1] - f[1]])
        ni = np.array([w[i+1][1] - w[i][1], w[i][0] - w[i+1][0]])
        Pi = np.dot(p, ni)
        Qi = np.dot(q, ni)
        if Pi == 0:
            if Qi < 0:
                vis = 0
                plt.plot([s_start[0], s_end[0]], [s_start[1], s_end[1]], c='blue')
                break
        else:
            t = -Qi / Pi
            x = s_start[0] + (s_end[0] - s_start[0]) * t
            y = s_start[1] + (s_end[1] - s_start[1]) * t
            ax.scatter(x, y)
            if Pi < 0:
                if t < t0:
                    vis = 0
                    plt.plot([s_start[0], s_end[0]], [s_start[1], s_end[1]], c='blue')
                    break
                if t < t1:
                    t1 = t
            else:
                if t > t1:
                    vis = 0
                    plt.plot([s_start[0], s_end[0]], [s_start[1], s_end[1]], c='blue')
                    break
                if t > t0:
                    t0 = t
    if vis:
        if t0 > t1:
            vis = 0
        else:
            print(t0, t1)
            if t0 >= 0:
                xo = s_start[0] + t0 * (s_end[0] - s_start[0])
                yo = s_start[1] + t0 * (s_end[1] - s_start[1])
            if t1 <= 1:
                xn = s_start[0] + t1 * (s_end[0] - s_start[0])
                yn = s_start[1] + t1 * (s_end[1] - s_start[1])
    if vis:
        if xo != xn and yo != yn:
            plt.plot([xo, xn], [yo, yn], c='r')
        plt.plot([s_start[0], xo], [s_start[1], yo], c='blue')
        plt.plot([xn, s_end[0]], [yn, s_end[1]], c='blue')

    plt.show()