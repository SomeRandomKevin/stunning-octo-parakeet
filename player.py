import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/ship_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 100))
        self.x = x
        self.y = y
        self.vel = 0
        self.leftMove = False
        self.rightMove = False
        self.rect = self.image.get_rect(midbottom=(x, y))

    def move(self):
        # Velocity if trying to move in both directions at the same time
        if self.leftMove and self.rightMove:
            if self.vel < 0:
                self.vel += 0.5
                self.vel = min(self.vel, 0)
            if self.vel > 0:
                self.vel -= 0.5
                self.vel = max(self.vel, 0)

        # Velocity if regular movement
        else:
            if self.leftMove:
                self.vel -= 0.5
                self.vel = max(self.vel, -10)  # max velocity left
            elif not self.rightMove and self.vel < 0:
                self.vel += 0.5  # slow down when not going left
                self.vel = min(self.vel, 0)
            if self.rightMove:
                self.vel += 0.5
                self.vel = min(self.vel, 10)  # max velocity right
            elif not self.leftMove and self.vel > 0:
                self.vel -= 0.5  # slow down when not going right
                self.vel = max(self.vel, 0)

        # Executing velocity as movement and boundaries
        self.x = max(0, self.x)
        self.x = min(920, self.x)
        self.x += self.vel

    #def shoot(self):

