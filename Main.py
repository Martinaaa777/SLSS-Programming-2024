# martina panosetti

# create a game:
  # Open a screen to show the environment.
  #Draw elements on the scene
  # Have elements on the screen that are user-controlled
  # Code is commented where appropriate and readable

import pygame
import random

# Pygame initialization
pygame.init()

# Constants definition
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
PLAYER_COLOR = (0, 255, 0)
ENEMY_COLOR = (255, 0, 0)

# Player class definition
class Player:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = (SCREEN_WIDTH - self.width) // 2
        self.y = SCREEN_HEIGHT - self.height - 20
        self.speed = 5

    def move_left(self):
        self.x -= self.speed
        if self.x < 0:
            self.x = 0

    def move_right(self):
        self.x += self.speed
        if self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width

    def draw(self, screen):
        pygame.draw.rect(screen, PLAYER_COLOR, (self.x, self.y, self.width, self.height))

# Enemy class definition
class Enemy:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = random.randint(0, SCREEN_WIDTH - self.width)
        self.y = -self.height
        self.speed = 3

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, ENEMY_COLOR, (self.x, self.y, self.width, self.height))

# Game window creation
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Shooter Game")

# Player and enemies initialization
player = Player()
enemies = []

# Main game function
def main():
    running = True
    clock = pygame.time.Clock()
    spawn_counter = 0
    spawn_delay = 60  # Spawn an enemy every 60 frames

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left()
                elif event.key == pygame.K_RIGHT:
                    player.move_right()

        # Enemies generation
        spawn_counter += 1
        if spawn_counter >= spawn_delay:
            enemies.append(Enemy())
            spawn_counter = 0

        # Enemies movement
        for enemy in enemies:
            enemy.move()

        # Collision detection
        for enemy in enemies:
            if enemy.y > SCREEN_HEIGHT:
                enemies.remove(enemy)
            elif player.x < enemy.x + enemy.width and player.x + player.width > enemy.x and \
                    player.y < enemy.y + enemy.height and player.y + player.height > enemy.y:
                print("Game Over!")
                running = False

        # Screen update
        screen.fill(BACKGROUND_COLOR)
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        pygame.display.flip()

        # Frame rate setting
        clock.tick(60)

    pygame.quit()

# Game start
if __name__ == "__main__":
    main()

