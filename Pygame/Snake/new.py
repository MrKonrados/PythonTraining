import pygame
from pygame.locals import *

WINDOW_SIZE = WIDTH, HEIHGT = 800, 600
GAME_NAME = "Snake"

FPS = 30

# SNAKE BODY
BLOCK_SIZE = 10

# MOVEMENT
SPEED = 1
RIGHT = 0, SPEED
LEFT = 0, -SPEED
UP = -SPEED, 0
DOWN = SPEED, 0

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (210, 105, 30)
RED = (255, 0, 0)
GREEN = (0, 128, 0)


class SnakePart(pygame.sprite.Sprite):
    rect = None

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



class Snake(pygame.sprite.LayeredUpdates):
    head = [WIDTH/2, HEIHGT/2]

    def __init__(self, length=10):
        super().__init__()
        for i in range(length):
            body_part = SnakePart(self.head[0] - (i * BLOCK_SIZE), self.head[1])
            self.add(body_part)

    def eat(self):
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass

    def move_up(self):
        pass

    def move_down(self):
        pass


class Game:
    is_running = False
    clock = pygame.time.Clock()

    def __init__(self):
        pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(GAME_NAME)
        pygame.init()



    def run(self):
        snake = Snake()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    break
                if event.type == KEYDOWN:
                    if event.key == K_w and current_direction != DOWN:
                        current_direction = UP
                    elif event.key == K_s and current_direction != UP:
                        current_direction = DOWN
                    elif event.key == K_d and current_direction != LEFT:
                        current_direction = RIGHT
                    elif event.key == K_a and current_direction != RIGHT:
                        current_direction = LEFT

            self.clock.tick(FPS)


    def stop(self):
        pass


if __name__ == "__main__":
    print("Starting game...")
    Game().run()
    print("The End")