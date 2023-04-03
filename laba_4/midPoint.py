import matplotlib.pyplot as plt
import numpy as np

import utils

def recMidPoint(mas1, st, se):

    d = utils.provLocation(mas1, st, se)
    #print(d)
    len_seg = np.sqrt((st[0]-se[0])*(st[0]-se[0])+(st[1]-se[1])*(st[1]-se[1]))

    if len_seg < 0.001:
        return

    if d == 1:
        plt.plot([st[0], se[0]], [st[1], se[1]], color='red')
        return
    if d == 2:
        plt.plot([st[0], se[0]], [st[1], se[1]], color='blue')
        return
    if d == 3:
        s = [(st[0] + se[0]) / 2, (st[1] + se[1]) / 2]
        plt.scatter(s[0], s[1], c='green')
        recMidPoint(mas1, st, s)
        recMidPoint(mas1, s, se)



def midPoint():
    print("window:")
    w = [int(i) for i in input().split()]
    print("start segment:")
    s_start = [int(i) for i in input().split()]
    print("end segment:")
    s_end = [int(i) for i in input().split()]

    utils.window(w)

    recMidPoint(w, s_start, s_end)

    plt.show()