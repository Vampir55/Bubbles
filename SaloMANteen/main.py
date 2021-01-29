# My new game SaloMANteen
import settings
import sys
import random as rnd
import pygame as pg


# Add new Classes
class GameWindow:
    screen = pg.display.set_mode((settings.HEIGHT, settings.WIDTH), 0, 32)
    clock = pg.time.Clock

    def __init__(self):
        screen = pg.display.set_mode((settings.HEIGHT, settings.WIDTH), 0, 32)
        pg.display.init()
        screen.fill((0, 0, 0))
        self.is_finished = False
        clock = pg.time.Clock

    def draw(self):
        clock = pg.time.Clock
        scene = GameScene()
        player = Player()
        while not self.is_finished:
            # Draw scene
            scene.drawscene()
            player.drawplayer()
            keys = pg.key.get_pressed()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_finished = True
            if keys[pg.K_RIGHT]:
                # Right arrow
                player.x += player.speed
            elif keys[pg.K_LEFT]:
                # Left arrow
                player.x -= player.speed
            elif keys[pg.K_SPACE]:
                pass  # Space key for jump
            else:
                pass  # Stand don't move
            # Draw objects
            pg.display.update()
            clock.tick(settings.FPS)


class GameObject:
    def __init__(self):
        self.x, self.y = 0, 0
        self.speed = 5
        self.is_moving = False
        self.is_collide = False
        self.picture = 0


class GameScene(GameObject):
    def drawscene(self):
        pg.draw.rect(GameWindow.screen, (255, 0, 255), (self.x, self.y, settings.HEIGHT, settings.WIDTH))



class Player(GameObject):
    def drawplayer(self):
        pg.draw.rect(GameWindow.screen, (25, 0, 255), (self.x, self.y, 20, 80))


class Enemy(GameObject):
    pass


class Block(GameObject):
    pass


def main():
    newWindow = GameWindow()
    newWindow.draw()


main()
