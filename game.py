import random

from player import *
from enemies import *


class Game:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.alive = False
        self.enemies = []
        self.enemy_bullets = []  # added here, so they don't disappear when enemy is killed
        self.spawn_cooldown = 150  # spawn rate (once per x ticks)
        self.spawn_counter = 150  # spawn timer
        # idea for removal list from chatGPT
        self.bullets_to_remove = []
        self.enemies_to_remove = []

        # groups and stuff with collision (guided by Coding with Russ) not working!!
        # create initial entities
        self.player = Player(width / 2 - 10, height - 150)
        # create sprite groups
        self.player_group = pygame.sprite.Group()
        self.enemies_group = pygame.sprite.Group()
        self.player_bullet_group = pygame.sprite.Group()
        self.enemy_bullet_group = pygame.sprite.Group()
        # add initial instances
        self.player_group.add(self.player)

    def spawn(self):  # spawning enemies
        if self.spawn_counter == 0:
            enemy = Enemy(random.randint(60, 940), 0)
            self.enemies.append(enemy)
            self.spawn_counter = self.spawn_cooldown
            self.enemies_group.add(enemy)

    def update(self):
        # updating player position
        self.player.update(self.screen)
        self.player.mask_rect.topleft = (self.player.x, self.player.y)
        # shooting and enemy spawn timers
        self.player.cooldown_counter -= 1
        self.player.cooldown_counter = max(self.player.cooldown_counter, 0)
        self.spawn_counter -= 1
        self.spawn_counter = max(self.spawn_counter, 0)

        # spawning and updating enemies
        if self.spawn_counter == 0:
            self.spawn()
        for enemy in self.enemies:
            enemy.update(self.screen)
            enemy.mask_rect.topleft = (enemy.x, enemy.y)
            if enemy.y > 1070:  # screen height + pixels for enemy to move off-screen
                self.enemies_to_remove.append(enemy)
            # enemy shooting timer, shooting and bullet updates
            enemy.cooldown_counter -= 1
            enemy.cooldown_counter = max(enemy.cooldown_counter, 0)
            # enemy shooting (bullet creation)
            if enemy.cooldown_counter == 0:
                bullet = Bullet(enemy.x + 20, enemy.y + 70, -5, enemy.bullet_image, enemy.bullet_size)
                self.enemy_bullets.append(bullet)
                enemy.cooldown_counter = enemy.cooldown
                self.enemy_bullet_group.add(self.enemy_bullets[-1])
        # updating each bullet
        for bullet in self.enemy_bullets:
            bullet.update(self.screen)
            bullet.mask_rect.topleft = (bullet.x, bullet.y)
            if not bullet.on_screen(self.height):  # prevent mass updating of off-screen bullets by elimination
                self.bullets_to_remove.append(bullet)
            else:  # bullet colliding with player ????
                if pygame.sprite.spritecollide(bullet, self.player_group, False, pygame.sprite.collide_mask):
                    print("dead True")
                    self.alive = False

        # player shooting (bullet creation)
        if self.player.shooting:
            if self.player.cooldown_counter == 0:
                bullet = Bullet(self.player.x + 40, self.player.y - 30, 10,
                                self.player.bullet_image, self.player.bullet_size)
                self.player.bullets.append(bullet)
                self.player.cooldown_counter = self.player.cooldown
                self.player_bullet_group.add(self.player.bullets[-1])
        # updating each bullet
        for bullet in self.player.bullets:
            bullet.update(self.screen)
            bullet.mask_rect.topleft = (bullet.x, bullet.y)
            if not bullet.on_screen(self.height):  # prevent mass updating of off-screen bullets by elimination
                self.bullets_to_remove.append(bullet)
            else:  # collision with enemy
                for enemy in self.enemies:
                    if pygame.sprite.spritecollide(bullet, self.enemies_group, False, pygame.sprite.collide_mask):
                        print("hit True")
                        self.enemies_to_remove.append(enemy)
                        self.bullets_to_remove.append(bullet)
                        break  # or else it removes every enemy?? don't understand

        # removing entities (idea from chatGPT, lower half improved by chatGPT)
        # if statements in each for loop is to prevent trying to remove something that has already been removed
        for bullet in self.bullets_to_remove:
            if bullet in self.player.bullets:
                self.player_bullet_group.remove(bullet)
                self.player.bullets.remove(bullet)
                bullet.kill()  # Remove the bullet sprite

        for dead_enemy in self.enemies_to_remove:
            for enemy in self.enemies:
                if dead_enemy.x == enemy.x and dead_enemy.y == enemy.y:  # check if exact same enemy by position
                    self.enemies_group.remove(enemy)
                    self.enemies.remove(enemy)
                    dead_enemy.kill()  # Remove the enemy sprite
                    break
