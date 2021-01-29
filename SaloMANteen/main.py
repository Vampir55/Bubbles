# My new game SaloMANteen
import settings
import sys
import random as rnd
import pygame as pg


# Add new Classes
class GameWindow:
    def __init__(self):
        screen = pg.display.set_mode((settings.HEIGHT, settings.WIGHT), 0, 32)
        pg.display.init()
        screen.fill((0, 0, 0))
        self.is_finished = False
        self.clock = pg.time.Clock

    def draw(self):
        while not self.is_finished:
            # Draw scene
            keys = pg.key.get_pressed()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_finished = True
                if keys[pg.K_RIGHT]:
                    pass  # Right arrow
                elif keys[pg.K_LEFT]:
                    pass  # Left arrow
                elif keys[pg.K_SPACE]:
                    pass  # Space key for jump
                else:
                    pass  # Stand don't move
            # Draw objects


class GameObject:
    pass


class GameScene(GameObject):
    pass


class Player(GameObject):
    pass


class Enemy(GameObject):
    pass


class Block(GameObject):
    pass


def main():
    newWindow = GameWindow()
    newWindow.draw()


main()
