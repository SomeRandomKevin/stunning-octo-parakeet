import time

import pygame

from game import *

# initialize pygame
pygame.init()
pygame.font.init()
width = 1000
height = 1000
screen = pygame.display.set_mode((width, height))
game = Game(screen, width, height)

# message
play_message = "press esc to play"
font = pygame.font.Font(None, 60)
play_message = font.render(play_message, True, (255, 255, 255))

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("sprites/icon.png")
pygame.display.set_icon(icon)

# background sprite
background = pygame.image.load("sprites/background.png")
background = pygame.transform.scale(background, (width, height))

# game loop
running = True
mask_shown = False
while running:
    if not game.alive:
        game = Game(screen, width, height)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.alive = True
                elif event.key == pygame.K_RETURN:
                    mask_shown = True

        screen.blit(play_message, (350, 500))
        pygame.display.update()

    if game.alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # actions start
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    game.player.leftMove = True
                elif event.key == pygame.K_d:
                    game.player.rightMove = True
                elif event.key == pygame.K_SPACE:
                    game.player.shooting = True
                elif event.key == pygame.K_RETURN:
                    mask_shown = True

            # actions stop
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    game.player.leftMove = False
                elif event.key == pygame.K_d:
                    game.player.rightMove = False
                elif event.key == pygame.K_SPACE:
                    game.player.shooting = False

        screen.blit(background, (0, 0))
        game.update()
        if mask_shown:
            screen.blit(game.player.mask.to_surface(), (game.player.mask_rect.x, game.player.mask_rect.y))
            for bullet in game.player.bullets:
                screen.blit(bullet.mask.to_surface(), (bullet.mask_rect.x, bullet.mask_rect.y))
            for enemy in game.enemies:
                screen.blit(enemy.mask.to_surface(), (enemy.mask_rect.x, enemy.mask_rect.y))
            for bullet in game.enemy_bullets:
                screen.blit(bullet.mask.to_surface(), (bullet.mask_rect.x, bullet.mask_rect.y))

        pygame.display.update()
        time.sleep(1 / 60)
