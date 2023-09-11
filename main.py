import pygame

# initialize pygame
pygame.init()
pygame.font.init()

# create the screen
screen = pygame.display.set_mode((1000, 1000))
width = screen.get_width()
height = screen.get_height()

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

    screen.blit(background, (0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        # Quit/anti-freeze
        if event.type == pygame.QUIT:
            running = False
