import random

import pygame
from pygame import font

pygame.time.set_timer(pygame.USEREVENT, 1000)
from Car import Car
from Enemy import Enemy
W = 512
H = 688
SCORE = 0
SPEED = 5
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
velocity = 0
roadx = 0
roady = 0
sc = pygame.display.set_mode((W, H))
cars = pygame.sprite.Group()
bonus = pygame.sprite.Group()
user = Car(0, pygame.image.load("red.png").convert_alpha())
USER = pygame.sprite.Group()
USER.add(user)
pictures = ["blue.png", "yellow.png", "black.png"]
bonuses = ["coin1.png", "coin5.png", "coin10.png"]
while 1:
    t = 100
    bonus_type = "boost"
    a = pygame.event.get()
    for i in a:
        if i.type == pygame.QUIT:
            pygame.quit()
        elif i.type == pygame.USEREVENT:
            j = random.randint(0, 2)
            i = random.randint(0,2)
            car_type = "racing"
            Enemy(W+W/400, pygame.image.load(pictures[j]).convert_alpha(), cars, car_type)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        user.rect.x += 5
    elif keys[pygame.K_LEFT]:
        user.rect.x -= 5
    elif keys[pygame.K_DOWN]:
        user.rect.y += 5
    elif keys[pygame.K_UP]:
        user.rect.y -= 5
    elif keys[pygame.K_SPACE]:
        velocity=10
        cars.update(SPEED)
    road = pygame.image.load("road.png").convert()
    roadx = roadx - velocity
    if roadx == 0:
        roadx = 500
    sc.fill(WHITE)
    sc.blit(road, [roadx - 500, roady])
    sc.blit(road, [roadx, roady])
    if pygame.sprite.spritecollide(user, cars, False):
        pygame.quit()
    USER.draw(sc)
    cars.draw(sc)
    USER.update()
    cars.update(SPEED)
    bonus.update(SPEED)
    SCORE += 3
    if SCORE % 500 == 0:
        SPEED += 2
    f = pygame.font.SysFont('arial', 30)
    stri = f.render("Score: " + str(SCORE), True, BLACK)
    sc.blit(stri, (0, 0))
    pygame.time.delay(20)
    pygame.display.update()
    USER.update()
    cars.update(SPEED)


