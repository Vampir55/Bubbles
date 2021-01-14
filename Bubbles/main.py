# My test project "Bubbles" to learning Classes and pygame lib
import pygame as pg


screen = pg.display.set_mode((600, 400), 0, 32)
pg.display.init()
screen.fill(WHITE)
pg.display.update()


class Bubble:
    x = 0
    y = 0
    radius = 1
    colors = [RED, GREEN, BLUE]
    color = colors[1]

disp.display.update()
 while 1:
     for i in disp.event.get():
        if i.type == disp.QUIT:
            disp.quit()

Bub1 = Bubble()
Bub1.color = 1
Bub1.radius = 20
Bub1.x=100
Bub1.y=200
drawbubble(Bub1)



def drawbubble(Bubble):
    print("drawing bubble", Bubble.x, Bubble.y, Bubble.radius, Bubble.color)
    pg.draw.circle(screen, Bubble.color, (Bubble.x, Bubble.y), Bubble.radius)



