import matplotlib.pyplot as plt

fig, ax = plt.subplots()
plt.grid()
plt.xlim(-20, 20)
plt.ylim(-20, 20)

def menu():
    print('1. Задание 1. Алгоритм Сазерленда-Коэна.')
    print('2. Задание 2. Алгоритм Цируса-Бека.')
    print('3. Задание 3. Алгоритм средней точки.')
    print('4. Выход.')

def drawRectangleLine(rx,ry,lx,ly,inx,iny):
    rx.append(rx[0])
    ry.append(ry[0])
    ax.plot(rx,ry,c='blue')
    if (len(inx)>0):
        ax.plot(lx,ly,c='black',linestyle = 'dashed')
        ax.plot(inx,iny,c='red')
    plt.show(block=False)
    

