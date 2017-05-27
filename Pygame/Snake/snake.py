import pygame
from pygame.locals import *

pygame.init()

# window size
WIDTH = 800
HEIGHT = 600

FPS = 10

# movement
STEP = 10
UP = (0, -STEP)
DOWN = (0, STEP)
LEFT = (-STEP, 0)
RIGHT = (STEP, 0)

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (210, 105, 30)
RED = (255, 0, 0)


class SnakeElement(pygame.sprite.Sprite):
    rect = None

    def __init__(self, pos_xy, direction=RIGHT):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = pos_xy[0] + direction[0]
        self.rect.y = pos_xy[1] + direction[1]

    def get_posxy(self):
        return (self.rect.x, self.rect.y)

    def update(self, is_head=False):
        if is_head:
            self.image.fill(RED)
        else:
            self.image.fill(WHITE)


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos_xy, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.x = pos_xy[0]
        self.rect.y = pos_xy[1]


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

game_speed = pygame.time.Clock()
is_running = True

snake = pygame.sprite.LayeredUpdates()
start_pos = (WIDTH / 2, HEIGHT / 2)
for i in range(10):
    snake.add(SnakeElement((start_pos[0] + (i * STEP), start_pos[1])))

current_direction = RIGHT
walls = pygame.sprite.Group()

# # create walls
wall_top = Wall((0, 0), WIDTH, 10)
wall_bottom = Wall((0, HEIGHT - 10), WIDTH, 10)
wall_left = Wall((0, 0), 10, HEIGHT)
wall_right = Wall((WIDTH - 10, 0), 10, HEIGHT)

walls.add(wall_top, wall_bottom, wall_left, wall_right)

all_sprites = pygame.sprite.Group(snake.sprites(), walls.sprites())

while is_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_running = False
        if event.type == KEYDOWN:
            if event.key == K_w and current_direction != DOWN:
                current_direction = UP
            elif event.key == K_s and current_direction != UP:
                current_direction = DOWN
            elif event.key == K_d and current_direction != LEFT:
                current_direction = RIGHT
            elif event.key == K_a and current_direction != RIGHT:
                current_direction = LEFT

    head = snake.get_top_sprite()
    head = SnakeElement((head.rect[0], head.rect[1]), direction=current_direction)  # new head
    snake.remove(snake.get_sprite(0))  # remove tail

    if pygame.sprite.spritecollide(head, all_sprites, False):
        is_running = False

    snake.add(head)  # add new element as a head

    for part in snake:
        if part == head:
            part.update(True)
        else:
            part.update()

    # Drawing
    screen.fill(BLACK)
    walls.update()

    walls.draw(screen)
    snake.draw(screen)

    pygame.display.flip()
    game_speed.tick(FPS)

pygame.quit()
exit()
