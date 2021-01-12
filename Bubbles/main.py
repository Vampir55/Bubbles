# My test project "Bubbles" to learning Classes and pygame lib
import pygame as pg


display = pg.display.set_mode((1000, 500))

class Bubble:
    x = 0
    y = 0
    radius = 1
    colors = ['RED', 'GREEN', 'BLUE']
    color = colors[1]


def main():
    return 0


def drawbubble(Bubble):
    print("drawing bubble", Bubble.x, Bubble.y, Bubble.radius, Bubble.color)
    pg.draw.circle(1, Bubble.color, (Bubble.x, Bubble.y), Bubble.radius)


main()  # call main function
