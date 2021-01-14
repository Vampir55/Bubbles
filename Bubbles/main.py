# My test project "Bubbles" to learning Classes and pygame lib

# Import libs and modules
import sys
import colors as colors
import pygame as pg


# Make new class "Bubble"
class Bubble:
    def __init__(self):
        radius = 10
        coordinates = x, y = (0, 0)
        color = (0, 0, 0)

    def draw(self):
        pass

    def collision(self):
        pass


def main():
    # stats main loop
    running = True
    while running:
        for event in pg.event.get():
            if event == pg.QUIT:
                running = False
            # there is main loop and asking for events


pg.display.init()
screen = pg.display.set_mode((640, 480), 0, 32)
screen.fill(colors.WHITE)
pg.display.flip()


main()
