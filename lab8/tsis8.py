import pygame
import random
import time
# import psycopg2

from pygame.locals import *
from pygame import mixer

# constants
WIDTH = 600
HEIGHT = 500

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# display
pygame.init()
pygame.display.set_caption("Endless Ride 1")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.Surface((WIDTH, HEIGHT))
road = pygame.Surface((300, HEIGHT))
clock = pygame.time.Clock()
road.fill((79, 81, 78))
bg.fill((76, 169, 5))
done = False

# game variables
coins = 0
score = 0
speed = 1

# texts and fonts
font = pygame.font.SysFont("Verdana", 90)
font_small = pygame.font.SysFont("Verdana", 22)
game_over = font.render("Game Over", True, RED)
text_rect = game_over.get_rect(center=(WIDTH / 2, HEIGHT / 2))

# background sound
mixer.music.load("media/background2.mp3")
mixer.music.play(-1)

# image
coin_image = pygame.image.load('media/coin.png')
flowers_image = pygame.image.load('media/pink_flower.png')


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('media/car2.png')
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.surface = pygame.Surface((55, 90))
        self.rect = self.surface.get_rect(center=(250, 400))

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < 480:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)

        if self.rect.left > 155:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 435:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT - 70)

    def update(self):
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.center = WIDTH / 2
            self.rect.bottom = HEIGHT - 70


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('media/enemy2.png')
        self.surface = pygame.Surface((55, 95))
        self.rect = self.surface.get_rect(center=(random.randint(180, 400), 0))

    def move(self):
        global score
        self.rect.move_ip(0, random.randint(speed, 5))
        if self.rect.bottom > HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(180, 400), 0)

    def after_hide(self):
        self.rect.center = (180, 0)


class Rectangle:
    def __init__(self, x=10, y=10, color=(255, 255, 255), width=20, height=30, sp=6):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.speed = sp
        self.hero = False
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def fall(self):
        if not self.hero:
            self.y += self.speed


class Coin:
    def __init__(self, x=10, y=10, color=(255, 255, 255), radius=30, sp=5, image=coin_image, is_coin=True):
        self.x = x
        self.y = y
        self.color = color
        self.speed = sp
        self.radius = radius
        self.image = image
        self.is_coin = is_coin
        self.hitbox = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        self.count = 0

    def draw(self):
        self.hitbox = pygame.Rect(self.x + 30, self.y - self.radius, self.radius * 2, self.radius * 2)
        self.count += 1
        if self.count > 79:
            self.count = 0
        screen.blit(pygame.transform.scale(self.image, (80, 80)), (self.x, self.y))

    def fall(self):
        global score
        self.y += self.speed
        if self.hitbox.colliderect(P1.rect) and self.is_coin:
            obstacles.remove(self)
            score += 1


P1 = Player()
E1 = Enemy()

obstacles = []

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 3000)

flowers = []
lines = []
line1 = Rectangle(298, -200, (251, 199, 11), 10, 150, 2)
line2 = Rectangle(298, 0, (251, 199, 11), 10, 150, 2)
line3 = Rectangle(298, 200, (251, 199, 11), 10, 150, 2)
line4 = Rectangle(298, 400, (251, 199, 11), 10, 150, 2)

lines.extend([line1, line2, line3, line4])


def spawner():
    if len(obstacles) < 3:
        obstacles.append(Coin(random.randrange(180, 400, 20), random.randrange(-500, -50, 100), (random.randint(
            100, 130), random.randint(40, 60), random.randint(150, 170)), 16))
    if len(flowers) < 20:
        flowers.append(Coin(random.randrange(0, 100, 20), random.randrange(-500, -50, 100), (random.randint(
            20, 30), random.randint(150, 170), random.randint(25, 50)), random.randrange(20, 40, 10),
                            image=flowers_image, is_coin=False))
        flowers.append(Coin(random.randrange(480, 560, 20), random.randrange(-500, -50, 100), (random.randint(
            20, 30), random.randint(150, 170), random.randint(25, 50)), random.randrange(20, 40, 10),
                            image=flowers_image, is_coin=False))


def drawCoins():
    global score
    text = font_small.render(f'Score:{score}', True, WHITE)
    screen.blit(text, (460, 20))


def drawLives():
    # text = font_small.render(f'Lives:{P1.lives}', True, (255, 255, 255))
    pos_x = 20
    # text = font_small.render('Lives:', True, (79, 81, 78))
    heart_image = pygame.image.load('media/heart.png')
    for i in range(P1.lives):
        screen.blit(pygame.transform.scale(heart_image, (30, 30)), (pos_x, 25))
        pos_x += 30
    # screen.blit(text, (10, 20))


def run():
    global speed
    global done
    while not done:
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                if speed >= 5:
                    speed = 1
                else:
                    speed += 1
            if event.type == QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True

        screen.blit(bg, (0, 0))
        screen.blit(road, (150, 0))

        spawner()

        pygame.draw.rect(screen, WHITE, pygame.Rect(155, 0, 10, HEIGHT))
        pygame.draw.rect(screen, WHITE, pygame.Rect(435, 0, 10, HEIGHT))

        for line in lines:
            line.draw()
            line.fall()
            if line.y > 500:
                line.y = -200
        for obs in obstacles:
            obs.draw()
        for obs in obstacles:
            obs.fall()
            if obs.y > 500:
                obstacles.remove(obs)
        for flower in flowers:
            flower.draw()
        for flower in flowers:
            flower.fall()
            if flower.y > 500:
                flowers.remove(flower)

        for entity in all_sprites:
            screen.blit(pygame.transform.scale(entity.image, (70, 120)), entity.rect)
            entity.move()

        if P1.lives > 0:
            if pygame.sprite.spritecollideany(P1, enemies):
                pygame.mixer.Sound('media/crash.wav').play()
                time.sleep(0.5)
                P1.hide()
                E1.after_hide()
                P1.lives -= 1
                pygame.display.update()
        else:
            time.sleep(2)
            screen.fill(WHITE)
            screen.blit(game_over, text_rect)
            pygame.display.update()
            time.sleep(2)
            done = True

        drawLives()
        drawCoins()
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)


run()
