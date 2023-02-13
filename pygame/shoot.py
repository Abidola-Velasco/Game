from random import randint

Nugget = Actor("cat")


def draw():
    screen.clear()
    Nugget.draw()


def place_Nugget():
    Nugget.x = randint(10, 650)
    Nugget.y = randint(10, 450)


place_Nugget()


def on_mouse_down(pos):
    if Nugget.collidepoint(pos):
        print("Nice shot!")
        place_Nugget()
    else:
        print("you missed!")
        quit()
