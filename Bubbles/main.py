# My test project "Bubbles" to learning Classes and pygame lib

# Import libs and modules
import sys
import random as rnd
import math
import settings
import colors
import pygame as pg


# Make new class "Bubble"
class Bubble:
    def __init__(self):
        self.x, self.y = 0, 0
        self.vx, self.vy = 0, 0
        self.radius = 10
        self.coordinates = (self.x, self.y)
        self.speed = (self.vx, self.vy)
        self.color = (0, 0, 0)
        self.r_length = 2*math.pi*self.radius

    def create(self, radius, coordinates, color):
        self.radius = radius
        self.coordinates = coordinates
        self.color = color

    def draw(self):
        self.vx = self.speed[0]
        self.vy = self.speed[1]
        self.x = self.coordinates[0] + self.vx
        self.y = self.coordinates[1] + self.vy
        self.coordinates = (self.x, self.y)
        pg.draw.circle(screen, self.color, self.coordinates, self.radius)
        pg.draw.circle(screen, colors.WHITE, (self.x+self.radius/2, self.y-self.radius/2), self.radius/5)
        pg.draw.arc(screen, colors.BLACK, (self.x-self.radius+2, self.y-self.radius-2, self.radius * 2,
                                           self.radius * 2), math.pi-0.2, 3/2 * math.pi+0.2, width=1)
        pg.draw.arc(screen, colors.BLACK, (self.x - self.radius + 4, self.y - self.radius - 4, self.radius * 2,
                                           self.radius * 2), math.pi+0.1, 3 / 2 * math.pi-0.1, width=1)
        pg.draw.arc(screen, colors.BLACK, (self.x - self.radius + 6, self.y - self.radius - 6, self.radius * 2,
                                           self.radius * 2), math.pi+0.4, 3 / 2 * math.pi-0.4, width=1)

    def test_collision(self, other_obj):
        if self.x + self.radius >= settings.WIDTH or self.x + self.radius <= 0:
            self.vx *= -1
        if self.y + self.radius >= settings.HEIGHT or self.y + self.radius <= 0:
            self.vy *= -1
        if (self.x + self.radius == other_obj.x - other_obj.radius) or \
                (self.y + self.radius == other_obj.y - other_obj.radius) or \
                (self.x - self.radius == other_obj.x + other_obj.radius) or \
                (self.y - self.radius == other_obj.y + other_obj.radius):
            self.vx *= -1
            self.vy *= -1
        self.speed = (self.vx, self.vy)

    def test_collision_circle(self, other_obj):
        for i_self in range(1, self.r_length):
            for i_other in range(1, other_obj.r_length):
                pass


def main():
    # Creating Bubbles
    rnd.seed()
    bubbles = []
    for num in range(0, settings.NUM_BUBBLES):
        rad = rnd.randrange(10, 40, 5)
        cord_x = rnd.randrange(50, settings.WIDTH, 50)
        cord_y = rnd.randrange(50, settings.HEIGHT, 50)
        spd_x = rnd.randint(1, 4)
        spd_y = rnd.randint(1, 4)
        clr_rnd = rnd.randint(0, len(colors.COLORS_LIST)-1)
        bubbles.append(Bubble())
        bubbles[num].create(rad, (cord_x, cord_y), colors.COLORS_LIST[clr_rnd])
        bubbles[num].speed = (spd_x, spd_y)

    # stats main loop
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        # there is main loop and asking for events
        # draw bubbles
        for num in range(0, settings.NUM_BUBBLES):
            bubbles[num].draw()
            p = 1
            if num+1 >= settings.NUM_BUBBLES:
                p = 0
            bubbles[num].test_collision(bubbles[num+p])

        # screen update
        pg.display.flip()
        pg.time.delay(settings.FPS)
        screen.fill(settings.BACKGROUND)

# Screen initialization
pg.display.init()
screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT), 0, 32)
pg.display.set_caption("Bubbles Game")
screen.fill(settings.BACKGROUND)
pg.display.flip()


main()
