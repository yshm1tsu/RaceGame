import pygame

W = 750
H = 700


class Car(pygame.sprite.Sprite):
    def __init__(self, x, surf):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, H // 2))
        self.image.set_colorkey((255, 255, 255))
        cars = pygame.sprite.Group()

    def update(self):
        if self.image.get_width() + self.rect.x >= W:
            self.rect.x = W - self.image.get_width()
        elif self.rect.x <= 0:
            self.rect.x = 0
        if self.image.get_height() + self.rect.y >= 4 * H // 5:
            self.rect.y = 4 * H // 5 - self.image.get_height()
        elif self.rect.y <= H // 5:
            self.rect.y = H // 5