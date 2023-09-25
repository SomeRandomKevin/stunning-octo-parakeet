import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/ship_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 100))
        self.x = x
        self.y = y
        self.leftMove = False
        self.rightMove = False
        self.vel = 0
        self.rect = self.image.get_rect(midbottom=(x, y))

    def move(self):
        if self.leftMove:
            self.vel += 0.5
            self.vel = min(self.vel, 10)
            self.x -= self.vel
            self.x = max(0, self.x)
        if self.rightMove:
            self.vel += 0.5
            self.vel = min(self.vel, 10)
            self.x += self.vel
            self.x = min(920, self.x)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprite/laser_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (5, 20))
        self.x = x
        self.y = y
        self.vel = 10
        self.rect = self.image.get_rect(midbottom=(x, y))
