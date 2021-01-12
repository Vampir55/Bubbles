# My test project "Bubbles" to learning Classes and pygame lib
import pygame as pg

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pg.display.set_mode((600, 400), 0, 32)
pg.display.init()
screen.fill(WHITE)
pg.display.update()


# class Bubble:
#     x = 0
#     y = 0
#     radius = 1
#     colors = [RED, GREEN, BLUE]
#     color = colors[1]
#
#
# def main(disp):
#     disp.display.update()
#     while 1:
#         for i in disp.event.get():
#             if i.type == disp.QUIT:
#                 disp.quit()
#
#
# def drawbubble(Bubble):
#     print("drawing bubble", Bubble.x, Bubble.y, Bubble.radius, Bubble.color)
#     pg.draw.circle(screen, Bubble.color, (Bubble.x, Bubble.y), Bubble.radius)
#

# main(pg)  # call main function
