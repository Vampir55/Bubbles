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
        self.v_radius = 0
        self.coordinates = (self.x, self.y)
        self.speed = (self.vx, self.vy)
        self.color = (0, 0, 0)
        self.r_length = 2*math.pi*self.radius
        self.score = 0
        self.is_alive = True

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
        rad = self.radius + self.v_radius
        if self.radius > 1:
            self.radius = rad
        else:
            self.radius = 0
        # Drawing
        pg.draw.circle(screen, self.color, self.coordinates, self.radius)
        pg.draw.circle(screen, colors.WHITE, (self.x+self.radius/2, self.y-self.radius/2), self.radius/5)
        pg.draw.arc(screen, colors.BLACK, (self.x-self.radius+2, self.y-self.radius-2, self.radius * 2,
                                           self.radius * 2), math.pi-0.2, 3/2 * math.pi+0.2, width=1)
        pg.draw.arc(screen, colors.BLACK, (self.x - self.radius + 4, self.y - self.radius - 4, self.radius * 2,
                                           self.radius * 2), math.pi+0.1, 3 / 2 * math.pi-0.1, width=1)
        pg.draw.arc(screen, colors.BLACK, (self.x - self.radius + 6, self.y - self.radius - 6, self.radius * 2,
                                           self.radius * 2), math.pi+0.4, 3 / 2 * math.pi-0.4, width=1)

    def test_collision(self, other_obj):
        collision_flag = False
        # test collisions with screen borders
        if self.x + self.radius >= settings.WIDTH or self.x - self.radius <= 0:
            self.vx *= -1
        if self.y + self.radius >= settings.HEIGHT or self.y - self.radius - settings.SCORE_HEIGHT <= 0:
            self.vy *= -1
        # test collisions with other objects
        if (self.x > other_obj.x - other_obj.radius) and \
                (self.x < other_obj.x + other_obj.radius) and \
                (self.y + self.radius == other_obj.y - other_obj.radius) and (self.vx > 0):
            self.vy *= -1
            collision_flag = True
        elif (self.x > other_obj.x - other_obj.radius) and \
                (self.x < other_obj.x + other_obj.radius) and \
                (self.y - self.radius == other_obj.y + other_obj.radius) and (self.vx < 0):
            self.vy *= -1
            collision_flag = True
        elif (self.y > other_obj.y - other_obj.radius) and \
                (self.y < other_obj.y + other_obj.radius) and \
                (self.x - self.radius == other_obj.x + other_obj.radius) and (self.vx < 0):
            self.vx *= -1
            collision_flag = True
        # elif (self.y > other_obj.y - other_obj.radius) and \
        #         (self.y < other_obj.y + other_obj.radius) and \
        #         (self.x + self.radius == other_obj.x - other_obj.radius) and (self.vx > 0):
        else:
            self.vx *= -1
            collision_flag = True
        self.speed = (self.vx, self.vy)
        return collision_flag

    def test_collision_circle(self, other_obj):  # FIXME
        for i_self in range(1, self.r_length):
            for i_other in range(1, other_obj.r_length):
                pass

    def test_mouse_pressed(self):
        m_pos = pg.mouse.get_pos()
        if (m_pos[0] < self.x + self.radius) and (m_pos[0] > self.x - self.radius) and \
                (m_pos[1] < self.y + self.radius) and (m_pos[1] > self.y - self.radius) and \
                (pg.mouse.get_pressed() == (True, False, False)):
            self.vx, self.vy = 0, 0
            self.v_radius = -1
        return self.score


def create_bubbles():
    # Creating Bubbles
    rnd.seed()
    bubbles = []
    for num in range(0, settings.NUM_BUBBLES):
        rad = rnd.randrange(15, 45, 5)
        cord_x = rnd.randrange(50+rad, settings.WIDTH-rad, 50)
        cord_y = rnd.randrange(50+settings.SCORE_HEIGHT+rad, settings.HEIGHT-settings.SCORE_HEIGHT-rad, 50)
        spd_x = rnd.randint(1, 4)
        spd_y = rnd.randint(1, 4)
        clr_rnd = rnd.randint(0, len(colors.COLORS_LIST) - 1)
        while colors.COLORS_LIST[clr_rnd] == settings.BACKGROUND:
            clr_rnd = rnd.randint(0, len(colors.COLORS_LIST)-1)
        # score colors settings
        if colors.COLORS_LIST[clr_rnd] == colors.RED:
            score_rnd = -100
        elif colors.COLORS_LIST[clr_rnd] == colors.CYAN:
            score_rnd = 50
        else:
            score_rnd = rnd.randint(0, 40)

        bubbles.append(Bubble())
        bubbles[num].create(rad, (cord_x, cord_y), colors.COLORS_LIST[clr_rnd])
        bubbles[num].speed = (spd_x, spd_y)
        bubbles[num].score = score_rnd
    return bubbles


def create_game_field(score, bubbles_num):
    pg.draw.rect(screen, colors.CYAN, (1, 1, settings.WIDTH-1, settings.SCORE_HEIGHT-6), width=5, border_radius=10)
    font = pg.font.Font(None, 46)
    text_score = font.render('Bubbles: ' + str(bubbles_num) + '   Score: ' + str(score), True, colors.LIME, None)
    screen.blit(text_score, (10, 10))


def message(text: str, sec: int):
    pg.draw.rect(screen, colors.BLUE, (settings.WIDTH/2-250, settings.HEIGHT/2-10, 500, settings.SCORE_HEIGHT), width=8, border_radius=20)
    font = pg.font.Font(None, 46)
    text_score = font.render(text, True, colors.CYAN, None)
    screen.blit(text_score, (settings.WIDTH/2-225, settings.HEIGHT/2))
    pg.display.flip()
    pg.time.delay(sec*1000)


def main():
    # Call function create bubbles
    bubbles = create_bubbles()
    score = 0
    message("Try not push RED bubbles!", 3)

    # stats main loop
    running = True
    while running:
        for event in pg.event.get():
            # there is main loop and asking for events
            if event.type == pg.QUIT:
                running = False

        # draw game field
        create_game_field(score, len(bubbles))

        # draw bubbles
        flag_endgame = True
        for num, bubble in enumerate(bubbles):
            bubble.draw()
            for num2, other_bubble in enumerate(bubbles):
                bubble.test_collision(other_bubble)

            bubble_score = bubble.test_mouse_pressed()
            if bubble.radius <= 1:
                score = score + bubble_score
                bubbles.remove(bubble)
            if bubble.color != colors.RED or num != 0:
                flag_endgame = False

        if flag_endgame:
            # Calling finish game function
            message('Game over! Your score is ' + str(score) + '!', 10)
            # running = False

        # screen update
        pg.display.flip()
        pg.time.delay(settings.FPS)
        screen.fill(settings.BACKGROUND)



# Screen initialization
pg.display.init()
pg.font.init()
screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT), 0, 32)
pg.display.set_caption("Bubbles Game")
screen.fill(settings.BACKGROUND)
pg.display.flip()


main()
