import pygame


class Ball(object):

    def __init__(self, x, y, game):
        self.game = game
        self.x = x
        self.y = y
        self.speed_x = self.speed_y = self.game.BALL_SPEED

    def move(self):
        if self.x == self.game.B_WIDTH or self.x == 0:
            self.speed_x *= -1
        if self.y == self.game.B_HEIGHT or self.y == 0:
            self.speed_y *= -1

        self.x += self.speed_x
        self.y += self.speed_y


    def draw(self):
        rect = pygame.Rect(self.x, self.y, self.game.BALL_SIZE, self.game.BALL_SIZE)
        pygame.draw.rect(self.game.displaySurface, self.game.WHITE, rect)
