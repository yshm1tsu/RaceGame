import random

import pygame

W = 750
H = 700
SPEED = 5
class Bonus(pygame.sprite.Sprite):
    def __init__(self, x, surf, group, my_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.add(group)
        self.rect = self.image.get_rect(center=(x, random.randint(H // 5, 4 * H // 5)))
        self.speed = SPEED
        self.my_type = my_type
        self.image.set_colorkey((255, 255, 255))
        self.count = 1

    def update(self, SPEED):
        self.speed = SPEED
        if self.rect.x <= 0:
            self.kill()
        else:
            if self.image.get_height() + self.rect.y >= (4 * H // 5):
                self.rect.y = 4 * H // 5 - self.image.get_height()
            elif self.rect.y <= H // 5:
                self.rect.y = H // 5
            self.rect.x -= self.speed