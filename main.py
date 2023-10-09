import pygame
import time
from player import *


class Game:
    def __init__(self):
        self.player = Player(450, 900)
        self.playerSprite = pygame.sprite.GroupSingle(self.player)

    def update(self):
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
            elif event.key == pygame.K_d:
                game.player.rightMove = False

        # shooting

    screen.blit(background, (0, 0))
    game.update()
    pygame.display.update()
    time.sleep(1/60)
