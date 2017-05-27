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


class SnakeElement(pygame.sprite.Sprite):
    def __init__(self, pos_xy, direction=RIGHT):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = pos_xy[0] + direction[0]
        self.rect.y = pos_xy[1] + direction[1]

    def get_posxy(self):
        return (self.rect.x, self.rect.y)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

game_speed = pygame.time.Clock()
is_running = True

start_pos = (WIDTH/2, HEIGHT/2)
snake = []
for i in range(10):
    snake.append(SnakeElement((start_pos[0] + (i * STEP), start_pos[1])))

all_sprites = pygame.sprite.Group()
all_sprites.add(snake)

current_direction = RIGHT

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

    all_sprites.remove(snake[0]) # remove tail from spirtes
    del snake[0] # remove tail from list

    head = snake[-1].get_posxy() # get head position
    new_head = SnakeElement(head, current_direction) # create new head

    # if head is colliding with part of snake then end game
    if pygame.sprite.spritecollide(new_head, all_sprites, False):
        is_running = False

    snake.append(new_head)

    all_sprites.add(snake)
    screen.fill(BLACK)
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()
    game_speed.tick(FPS)

pygame.quit()
exit()
