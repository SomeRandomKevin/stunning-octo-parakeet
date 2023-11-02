import pygame
from bullet import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/invader_1.png')
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (60, 70)).convert_alpha()
        self.bullet_image = 'sprites/enemy_laser_1.png'
        self.bullet_size = (20, 20)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_rect = self.mask.get_bounding_rects()[0]
        self.vel = 1
        self.cooldown = 70
        self.cooldown_counter = self.cooldown

    def update(self, window):
        window.blit(self.image, (self.x, self.y))
        self.y += self.vel
        self.rect.topleft = [self.x, self.y]
