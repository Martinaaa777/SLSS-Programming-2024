# pygame-exercise-jewelthief.py
# Clone of Jewel Thief Game

import random
import pygame as pg

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
WIDTH = 1280  # Pixels
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)

NUM_COINS = 100
NUM_ENEMIES = 5


class Player(pg.sprite.Sprite):
    # TODO: Change Mario image depending on facing direction
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/mario.webp")
        self.images = [
            pg.image.load("./Images/mario.webp"),
            pg.transform.flip(pg.image.load("./Images/mario.webp"), True, False),
        ]

        self.image = self.images[0]

        self.rect = self.image.get_rect()

        self.facing = 0  # 0 is right, 1 is left

    def update(self):
        """Updates the location of sprite to the mouse cursor"""
        self.rect.centerx = pg.mouse.get_pos()[0]
        self.rect.centery = pg.mouse.get_pos()[1]
        next_pos = pg.mouse.get_pos()

        if self.rect.centerx > next_pos[0]:
            self.facing = 1
        elif self.rect.centerx < next_pos[0]:
            self.facing = 0

        self.rect.center = next_pos
        self.image = self.images[self.facing]


class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("./Images/coin.png")
        self.rect = self.image.get_rect()
        # Randomize initial location
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)


class Goomba(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/goomba.png")
        self.rect = self.image.get_rect()

        # Spawn in a random location
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)

        # Set initial velocity to some random value
        self.vel_x = random.choice((-6, -5, -4, 4, 5, 6))
        self.vel_y = random.choice((-6, -5, -4, 4, 5, 6))

    def update(self):
        """Move the goomba and bounce it off the edge of the window"""
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Bounce
        if self.rect.left < 0:
            self.rect.left = 0  # keep it inside the screen
            self.vel_x = -self.vel_x
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.vel_x = -self.vel_x
        if self.rect.top < 0:
            self.rect.top = 0
            self.vel_y = -self.vel_y
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.vel_y = -self.vel_y


def start():
    """Environment Setup and Game Loop"""

    pg.init()
    pg.mouse.set_visible(False)

    # --Game State Variables--
    # --Game St
    # ate Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    score = 0

    # -- Sprite Groups
    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    # Coin sprites
    coin_sprites = pg.sprite.Group()
    enemy_sprites = pg.sprite.Group()

    # Create coins
    for _ in range(NUM_COINS):
        coin = Coin()

        all_sprites.add(coin)
        coin_sprites.add(coin)
    # Create a player and store it in a variable
    player = Player()

    all_sprites.add(player)

    for _ in range(NUM_ENEMIES):
        enemy = Goomba()
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)

    pg.display.set_caption("Jewel Thief Clone (Don't sue us Nintendo)")

    # --Main Loop--
