import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/invader_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 70))
        self.bullet_image = pygame.image.load('sprites/enemy_laser_1.png').convert_alpha()
        self.bullet_image = pygame.transform.scale(self.bullet_image, (5, 10))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.vel = 0
        self.shooting = False
        self.bullets = []
        self.cooldown = 50
        self.cooldown_counter = self.cooldown

