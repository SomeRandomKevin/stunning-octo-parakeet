import pygame.sprite


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, vel, image, bullet_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, bullet_size).convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_rect = self.mask.get_bounding_rects()[0]
        self.vel = vel

    def update(self, window):
        window.blit(self.image, (self.x, self.y))
        self.y -= self.vel
        self.rect.topleft = [self.x, self.y]

    def on_screen(self, height):
        return height >= self.y >= 0
