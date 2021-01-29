# My new game SaloMANteen
import settings
import sys
import random as rnd
import pygame as pg


# Add new Classes
class GameWindow:
    screen = pg.display.set_mode((settings.HEIGHT, settings.WIDTH), 0, 32)
    clock = pg.time.Clock()

    def __init__(self):
        screen = pg.display.set_mode((settings.HEIGHT, settings.WIDTH), 0, 32)
        pg.display.init()
        screen.fill((0, 0, 0))
        self.is_finished = False

    def draw(self):
        clock = pg.time.Clock()
        scene = GameScene()
        scene.create()
        player = Player()
        player.y = settings.WIDTH - 20 - settings.player_WIDTH
        while not self.is_finished:
            # Draw scene
            scene.drawscene()
            player.drawplayer()
            keys = pg.key.get_pressed()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_finished = True
            if keys[pg.K_RIGHT] and player.x < settings.HEIGHT/2-settings.player_HEIGHT:
                # Right arrow
                player.x += player.speed
            if keys[pg.K_RIGHT] and player.x == settings.HEIGHT/2-settings.player_HEIGHT:
                # Right arrow
                scene.x -= scene.speed
            if keys[pg.K_LEFT] and player.x >= 5:
                # Left arrow
                player.x -= player.speed
            if not player.is_jump:
                if keys[pg.K_SPACE]:
                    # Space key for jump
                    player.is_jump = True
            else:
                if player.jump_count <= 0 and player.jump_count >= -10:
                    player.y -= (player.jump_count ** 2) / 2
                elif player.jump_count <= 10:
                    player.y += (player.jump_count ** 2) / 2
                player.jump_count += 1
                if player.jump_count > 10:
                    player.jump_count = -10
                    player.is_jump = False

            # Draw objects
            pg.display.update()
            self.screen.fill((255, 255, 0))
            clock.tick(settings.FPS)


class GameObject:
    def __init__(self):
        self.x, self.y = 0, 0
        self.speed = 5
        self.is_moving = False
        self.is_collide = False
        self.picture = 0


class GameScene(GameObject):
    blocks = []

    def create(self):
        for count in range(1, 10):
            self.blocks.append(Block())
            self.blocks[count-1].x = rnd.randint(0, settings.HEIGHT)
            self.blocks[count-1].y = rnd.randint(0, settings.WIDTH)

    def drawscene(self):
        for count in range(1, 10):
           self.blocks[count-1].create()





class Player(GameObject):
    jump_count = -10
    is_jump = False

    def drawplayer(self):
        pg.draw.rect(GameWindow.screen, (25, 0, 255), (self.x, self.y, settings.player_HEIGHT, settings.player_WIDTH))


class Enemy(GameObject):
    pass


class Block(GameObject):
    def create(self):
        pg.draw.rect(GameWindow.screen, (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255)),
                     (self.x, self.y, rnd.randint(10, 40), rnd.randint(10, 40)))


def main():
    newWindow = GameWindow()
    newWindow.draw()


main()
