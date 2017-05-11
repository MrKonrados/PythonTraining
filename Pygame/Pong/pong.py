import sys, pygame
from pygame.locals import *
from ball import Ball

class Game(object):
    # Window width and height
    W_WIDTH = 640
    W_HEIGHT = 480

    # Board width and height
    B_WIDTH = 64
    B_HEIGHT = 48

    # Paddle width and height
    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 4

    BALL_SIZE = 15
    BALL_SPEED = 1

    # Colors
    WHITE = pygame.Color(255, 255, 255)
    BLACK = pygame.Color(0, 0, 0)

    FPS = 30

    def __init__(self):
        pygame.init()
        fpsClock = pygame.time.Clock()
        self.displaySurface = pygame.display.set_mode((self.W_WIDTH, self.W_HEIGHT))
        pygame.display.set_caption("Pong!")

        self.ball = Ball(10, 10, self)

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.displaySurface.fill(self.BLACK)
            self.ball.move()
            self.draw()
            pygame.display.update()
            fpsClock.tick(self.FPS)

    def draw(self):
        self.ball.draw()

Game()