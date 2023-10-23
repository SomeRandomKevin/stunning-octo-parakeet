class Bullet:
    def __init__(self, x, y, vel, image):
        self.image = image
        self.x = x
        self.y = y
        self.vel = vel
        self.rect = self.image.get_rect(midbottom=(x, y))

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= self.vel

    def on_screen(self, height):
        return height >= self.y >= 0
