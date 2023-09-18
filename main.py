import pygame
from entities import *


class Game:
    def __init__(self):
        self.player = pygame.sprite.GroupSingle(Player((450, 900)))

    def update(self):
        self.player.draw(screen)


# initialize pygame
pygame.init()
pygame.font.init()
width = 1000
height = 1000
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
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

    screen.blit(background, (0, 0))
    game.update()
    pygame.display.update()
    clock.tick(60)
