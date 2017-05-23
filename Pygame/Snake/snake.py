import pygame
from pygame.locals import *

pygame.init()

# window size
WIDTH = 800
HEIGHT = 600

FPS = 30

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class SnakeElement(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += 1

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

game_speed = pygame.time.Clock()
is_running = True


sprites = pygame.sprite.Group()
for i in range(5):
    sprites.add(SnakeElement(10*i,10))

while is_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_running = False

    screen.fill(BLACK)

    sprites.update()
    sprites.draw(screen)

    pygame.display.flip()
    game_speed.tick(FPS)

pygame.quit()
exit()