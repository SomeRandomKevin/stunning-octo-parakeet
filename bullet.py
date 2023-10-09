import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprite/laser_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (5, 20))
        self.x = x
        self.y = y
        self.vel = 10
        self.rect = self.image.get_rect(midbottom=(x, y))

    def move(self):
        self.y -= self.vel
