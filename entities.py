import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/ship_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 100))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(midbottom=(x, y))
