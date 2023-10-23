import pygame
from bullet import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/invader_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 70))
        self.bullet_image = pygame.image.load('sprites/enemy_laser_1.png').convert_alpha()
        self.bullet_image = pygame.transform.scale(self.bullet_image, (20, 20))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.vel = 1
        self.shooting = False
        self.bullets = []
        self.cooldown = 50
        self.cooldown_counter = self.cooldown

    def move(self):
        self.y += self.vel

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def shoot(self):
        if self.cooldown_counter == 0:
            bullet = Bullet(self.x + 20, self.y + 20, -10, self.bullet_image)
            self.bullets.append(bullet)
            self.cooldown_counter = self.cooldown
