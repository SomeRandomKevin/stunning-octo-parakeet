import pygame


class Bullet:
    def __init__(self, x, y, image):
        self.image = image
        self.x = x
        self.y = y
        self.vel = 10
        self.rect = self.image.get_rect(midbottom=(x, y))

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= self.vel

    def on_screen(self, height):
        return height >= self.y >= 0
