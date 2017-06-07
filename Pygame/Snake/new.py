import pygame, math
from pygame.locals import *

WINDOW_SIZE = WIDTH, HEIHGT = 800, 600
GAME_NAME = "Snake"

FPS = 30

# SNAKE BODY
BLOCK_SIZE = 10

# MOVEMENT
SPEED = 1
UP = (0, -SPEED)
DOWN = (0, SPEED)
LEFT = (-SPEED, 0)
RIGHT = (SPEED, 0)

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (210, 105, 30)
RED = (255, 0, 0)
GREEN = (0, 128, 0)


class SnakeHead(pygame.sprite.Sprite):
    rect = None
    direction = RIGHT
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, direction=RIGHT):
        self.direction = direction

    def update(self):

        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]




class SnakePart(pygame.sprite.Sprite):
    rect = None
    direction = []
    def __init__(self, x, y, parent):
        super().__init__()
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.parent = parent

    def update(self):
        parent_x = self.parent.rect.x
        parent_y = self.parent.rect.y

        print(self.parent.rect)

        dx, dy = parent_x - self.rect.x, parent_y - self.rect.y
        dist = math.hypot(dx, dy)

        dx, dy = dx / dist, dy / dist

        self.direction = [dx*1, dy*1]
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]


# class Snake(pygame.sprite.LayeredUpdates):
#     head = [WIDTH/2, HEIHGT/2]
#
#     def __init__(self, length=10):
#         super().__init__()
#         for i in range(length):
#             body_part = SnakePart(self.head[0] - (i * BLOCK_SIZE), self.head[1])
#             self.add(body_part)
#
#     def eat(self):
#         pass
#
#     def move_to(self, direction=RIGHT):
#         pass



all_sprites = pygame.sprite.Group()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(GAME_NAME)

pygame.init()
clock = pygame.time.Clock()

head = SnakeHead(60,50)
body = SnakePart(40, 50, head)

all_sprites.add(head)
all_sprites.add(body)

current_direction = RIGHT

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_w and current_direction != DOWN:
                head.direction = UP
            elif event.key == K_s and current_direction != UP:
                head.direction = DOWN
            elif event.key == K_d and current_direction != LEFT:
                head.direction = RIGHT
            elif event.key == K_a and current_direction != RIGHT:
                head.direction = LEFT
            elif event.key == K_ESCAPE:
                pygame.quit()
                exit()

    # head.move(current_direction)
    all_sprites.update()
    # body.update()
    # body.folwlow_parent(head)


    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

