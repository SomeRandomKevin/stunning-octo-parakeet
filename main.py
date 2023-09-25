import pygame
import time
from entities import *


class Game:
    def __init__(self):
        self.player = Player(450, 900)
        self.playerSprite = pygame.sprite.GroupSingle(self.player)

    def update(self):
        # movement update (moved to entities.py)
        """if self.leftMove:
            self.player.vel += 0.75
            self.player.vel = min(self.player.vel, 10)
            self.playerSprite.sprite.rect.x -= self.player.vel
            self.playerSprite.sprite.rect.x = max(0, self.playerSprite.sprite.rect.x)
        if self.rightMove:
            self.player.vel += 0.75
            self.player.vel = min(self.player.vel, 10)
            self.playerSprite.sprite.rect.x += self.player.vel
            self.playerSprite.sprite.rect.x = min(920, self.playerSprite.sprite.rect.x)"""
        self.player.move()
        self.playerSprite.sprite.rect.x = self.player.x
        self.playerSprite.draw(screen)


# initialize pygame
pygame.init()
pygame.font.init()
width = 1000
height = 1000
screen = pygame.display.set_mode((width, height))
game = Game()


# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("sprites/icon.png")
pygame.display.set_icon(icon)

# set sprites
# background sprite
background = pygame.image.load("sprites/background.png")
background = pygame.transform.scale(background, (width, height))

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # left and right movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                game.player.leftMove = True
            elif event.key == pygame.K_d:
                game.player.rightMove = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                game.player.leftMove = False
                game.player.vel = 0
            elif event.key == pygame.K_d:
                game.player.rightMove = False
                game.player.vel = 0

        # shooting

    screen.blit(background, (0, 0))
    game.update()
    pygame.display.update()
    time.sleep(1/60)
