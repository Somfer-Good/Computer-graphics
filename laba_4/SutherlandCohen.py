import matplotlib.pyplot as plt

import utils

def SutherlandCohen():

    print("Фигура:")
    w = [int(i) for i in input().split()]
    print("Начало отрезка:")
    s_start = [int(i) for i in input().split()]
    print("Конец отрезка:")
    s_end = [int(i) for i in input().split()]

    Ax = w[0]
    Ay = w[1]
    Bx = w[2]
    By = w[3]

    d = utils.provLocation(w, s_start, s_end)

    if d == 1:
        utils.window(w)
        plt.plot([s_start[0], s_end[0]], [s_start[1], s_end[1]], color='r')

    if d == 2:
        utils.window(w)
        plt.plot([s_start[0], s_end[0]], [s_start[1], s_end[1]], color='g')

    if d == 3:
        A = s_end[1] - s_start[1]
        B = s_end[0] - s_start[0]
        C = s_start[1] * B - s_start[0] * A

        if A == 0 or B == 0:
            if A == 0:
                p1 = [Ax, s_start[1]]
                p2 = [Bx, s_start[1]]
                ans = []
                ans = utils.provSegment(p1, ans, s_start, s_end, w)
                ans = utils.provSegment(p2, ans, s_start, s_end, w)
                utils.visual(w, s_start, s_end, ans)
            else:
                p1 = [s_start[0], Ay]
                p2 = [s_start[0], By]
                ans = []
                ans = utils.provSegment(p1, ans, s_start, s_end, w)
                ans = utils.provSegment(p2, ans, s_start, s_end, w)
                #print(ans)
                utils.visual(w, s_start, s_end, ans)

        else:
            y = (A * Ax + C) / B
            p1 = [Ax, y]

            x = (B * By - C) / A
            p2 = [x, By]

            y = (A * Bx + C) / B
            p3 = [Bx, y]

            x = (B * Ay - C) / A
            p4 = [x, Ay]
            ans = []
            ans = utils.provSegment(p1, ans, s_start, s_end, w)
            ans = utils.provSegment(p2, ans, s_start, s_end, w)
            ans = utils.provSegment(p3, ans, s_start, s_end, w)
            ans = utils.provSegment(p4, ans, s_start, s_end, w)
            if len(ans) > 2:
                if ans[0][0] == ans[1][0] and ans[0][1] == ans[1][1]:
                    ans = [ans[0], ans[2]]
                else:
                    ans = [ans[0], ans[1]]

            utils.visual(w, s_start, s_end, ans)

    plt.show()
