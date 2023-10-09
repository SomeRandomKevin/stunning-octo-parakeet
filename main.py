import time
from player import *


class Game:
    def __init__(self):
        self.player = Player(450, 900)
        self.playerSprite = pygame.sprite.GroupSingle(self.player)

    def update(self):
        self.player.move()
        self.player.cooldown_counter -= 1
        self.player.cooldown_counter = max(self.player.cooldown_counter, 0)
        if self.player.shooting:
            self.player.shoot()
        for bullet in self.player.bullets:
            bullet.move()
            bullet.draw(screen)
            if not bullet.on_screen(height):
                del bullet
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
            elif event.key == pygame.K_SPACE:
                game.player.shooting = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                game.player.leftMove = False
            elif event.key == pygame.K_d:
                game.player.rightMove = False
            elif event.key == pygame.K_SPACE:
                game.player.shooting = False

        # shooting

    screen.blit(background, (0, 0))
    game.update()
    pygame.display.update()
    time.sleep(1/60)
