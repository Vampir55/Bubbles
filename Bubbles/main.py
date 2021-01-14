# My test project "Bubbles" to learning Classes and pygame lib

# Import libs and modules
import sys
import colors as colors
import pygame as pg


# Make new class "Bubble"
class Bubble:
    def __init__(self):
        self.radius = 10
        self.coordinates = x, y = (0, 0)
        self.speed = vx, vy = (0, 0)
        self.color = (0, 0, 0)

    def create(self, radius, coordinates, color):
        self.radius = radius
        self.coordinates = coordinates
        self.color = color

    def draw(self):
        self.coordinates += self.speed
        pg.draw.circle(screen, self.color, self.coordinates, self.radius)

    def collision(self):
        pass


def main():
    # stats main loop
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        # there is main loop and asking for events
        # create Bubbles and draw it
        bubble = Bubble()
        bubble.create(20, (100, 100), colors.RED)
        bubble.speed = (1, 1)
        bubble.draw()
        pg.display.flip()

# Screen initialization
pg.display.init()
screen = pg.display.set_mode((640, 480), 0, 32)
pg.display.set_caption("Bubbles Game")
screen.fill(colors.WHITE)
pg.display.flip()


main()
