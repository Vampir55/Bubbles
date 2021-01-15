# My test project "Bubbles" to learning Classes and pygame lib

# Import libs and modules
import sys
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



def main():
    # Creating Bubbles
    bubble = Bubble()
    bubble.create(20, (100, 100), colors.RED)
    bubble.speed = (1, 1)
    bubble2 = Bubble()
    bubble2.create(40, (200, 400), colors.GREEN)
    bubble2.speed = (1, 2)
    # stats main loop
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        # there is main loop and asking for events
        # draw bubbles
        bubble.draw()
        bubble.test_collision(bubble2)
        bubble2.draw()
        bubble2.test_collision(bubble)
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
