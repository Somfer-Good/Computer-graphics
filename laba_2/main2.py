import simple_draw as sd
import random

N=5

flake=[]
size=[]

def addFlake(count=5):
    for i in range(0,count):
        x=random.randint(-10, 300)
        y=random.randint(600, 700)
        size.append(random.randint(10, 30))
        flake.append(sd.get_point(x, y))

def removeFlake(i):
    flake.pop(i)
    size.pop(i)
    addFlake(1)

def statusFlake(i):
    if flake[i].x>700 or flake[i].y<0 or flake[i].x<0:
        removeFlake(i)

def moveFlake():
    s=len(flake)
    for i in range(0,s):
        flake[i].x+=random.randint(-20, 20)
        flake[i].y-=random.randint(0, 20)
        statusFlake(i)


addFlake(N)
while True:
    sd.clear_screen()
    pass
    while True:
        sd.clear_screen()
        for i in range(0,len(flake)):
            sd.snowflake(center=flake[i], length=size[i])
        moveFlake()
        print(len(flake))
        print(len(size))
        sd.sleep(0.1)