import pygame


class Paddle(object):
    """A paddle class."""
    x, y = 0

    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.x = y

    def draw(self):
        rect = pygame.Rect(self.x, self.y, self.game.BALL_SIZE)
        pygame.draw.rect(self.game.displaySurface, self.game.WHITE, rect)