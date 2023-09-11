import pygame

# initialize pygame
pygame.init()
pygame.font.init()

# create the screen
height = 1000
width = 1000
screen = pygame.display.set_mode((width, height))

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("sprites/icon.png")
pygame.display.set_icon(icon)

# set sprites
# background sprite
background = pygame.image.load("sprites/background.jpg")
background = pygame.transform.scale(background, (width, height/3))

# game loop
running = True
while running:
    screen.blit(background, (width, 0))
    screen.blit(background, (width, height/3))
    screen.blit(background, (width, 2*height/3))

    for event in pygame.event.get():
        # Quit/anti-freeze
        if event.type == pygame.QUIT:
            running = False
