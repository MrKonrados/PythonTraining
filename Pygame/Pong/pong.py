import pygame
from pygame.locals import *

pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")


class Ball(Rect):
    _stepx = _stepy = 10

    def __init__(self, paddle1):
        self.x, self.y = screen.get_size()
        Rect.__init__(self, (self.x / 2, self.y / 2), (10, 10))
        self.paddles = paddle1

    def move(self):
        if self.right > width or self.left < 0:
            self._stepx *= -1

        if self.bottom > height or self.top < 0:
            self._stepy *= -1

        if self.colliderect(self.paddles):
            self._stepx *= -1

        self.x += self._stepx
        self.y += self._stepy

    def draw(self):
        pygame.draw.rect(screen, WHITE, self)


class Paddle(Rect):
    def __init__(self):
        self.x = 30
        self.y = height / 2
        Rect.__init__(self, (self.x, self.y), (10, 300))
        self.centery = self.y

    def move(self, step):
        print(self.top, self.bottom)
        if self.top > 0 and self.bottom < height:
            self.y += step


    def draw(self):
        pygame.draw.rect(screen, WHITE, self)


def main():
    fps = pygame.time.Clock()
    p1 = Paddle()
    ball = Ball(p1)
    step = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                if event.key == K_w:
                    print(event.type)
                    step = -10
                if event.key == K_s:
                    print(event.type)
                    step = 10
            if event.type == KEYUP:
                step = 0

        screen.fill(BLACK)

        p1.move(step)
        ball.move()

        p1.draw()
        ball.draw()

        pygame.display.flip()
        fps.tick(60)


if __name__ == "__main__": main()
