Nugget = Actor("character")
Nugget.pos = 100, 50

WIDTH = 500
HEIGHT = Nugget.height + 20

def draw():
    screen.clear()
    screen.fill((255, 255, 255))
    Nugget.draw()

def update():
    Nugget.left = Nugget.left +2
    if Nugget.left > WIDTH:
        Nugget.right = 0
