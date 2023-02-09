Nugget = Actor("character")
Nugget.pos = 100, 50

WIDTH = 500
HEIGHT = Nugget.height + 20


def draw():
    screen.clear()
    screen.fill((255, 0, 0))
    Nugget.draw()


def update():
    Nugget.left = Nugget.left + 2
    if Nugget.left > WIDTH:
        Nugget.right = 0


Nugget.topright = 0, 10


def on_mouse_down(pos):
    if Nugget.collidepoint(pos):
        set_character()


def set_character():
    Nugget.image = "charactertophat"
    sounds.eep.play()
    clock.schedule_unique(set_character, 1.0)
