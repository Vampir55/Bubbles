# My test project "Bubbles" to learning Classes and pygame lib
from pygame import draw
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


main()  # call main function
