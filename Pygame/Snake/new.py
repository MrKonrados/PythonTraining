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



class SnakeTail(SnakeHead):
    rect = None
    direction = []
    def __init__(self, x, y, parent):
        super().__init__(x,y)
        self.parent = parent
        self.image.fill(WHITE)

    def update(self):
        follow_distance = BLOCK_SIZE + 3
        parent_x = self.parent.rect.x
        parent_y = self.parent.rect.y

        dx, dy = parent_x - self.rect.x, parent_y - self.rect.y

        print(dx, dy)

        dist = math.hypot(dx, dy)

        if (dist >  follow_distance):
            too_far = dist - follow_distance
            dx, dy = (dx / dist) , (dy / dist)
            self.rect.x += dx
            self.rect.y += dy

all_sprites = pygame.sprite.Group()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(GAME_NAME)

pygame.init()
clock = pygame.time.Clock()

head = SnakeHead(WIDTH/2, HEIHGT/2)
all_sprites.add(head)

body_1 = SnakeTail(WIDTH/2 - 10, HEIHGT/2, head); all_sprites.add(body_1)
# body_2 = SnakeTail(WIDTH/2 - 20, HEIHGT/2, body_1); all_sprites.add(body_2)
# body_3 = SnakeTail(WIDTH/2 - 30, HEIHGT/2, body_2); all_sprites.add(body_3)
# body_4 = SnakeTail(WIDTH/2 - 40, HEIHGT/2, body_3); all_sprites.add(body_4)
# body_5 = SnakeTail(WIDTH/2 - 50, HEIHGT/2, body_4); all_sprites.add(body_5)
# body_6 = SnakeTail(WIDTH/2 - 60, HEIHGT/2, body_5); all_sprites.add(body_6)
# body_7 = SnakeTail(WIDTH/2 - 70, HEIHGT/2, body_6); all_sprites.add(body_7)
# body_8 = SnakeTail(WIDTH/2 - 80, HEIHGT/2, body_7); all_sprites.add(body_8)




current_direction = RIGHT

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_w and current_direction != DOWN:
                current_direction = UP
            elif event.key == K_s and current_direction != UP:
                current_direction = DOWN
            elif event.key == K_d and current_direction != LEFT:
                current_direction = RIGHT
            elif event.key == K_a and current_direction != RIGHT:
                current_direction = LEFT
            elif event.key == K_ESCAPE:
                pygame.quit()
                exit()

    head.move(current_direction)
    all_sprites.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

