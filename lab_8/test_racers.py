import random

import pygame

pygame.init()

HEIGHT, WIDTH = 600, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
background = pygame.image.load('./materials/AnimatedStreet.png')
pygame.display.set_caption('Street Racer')
font_small = pygame.font.SysFont("Verdana", 20)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./materials/Enemy.png')

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect.width // 2, WIDTH - self.rect.width // 2), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.top > HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(self.rect.width // 2, WIDTH - self.rect.width // 2), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./materials/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressed = pygame.key.get_pressed()
        if self.rect.left > 5 and pressed[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH - 5 and pressed[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)


def main():
    running = True

    player = Player()
    enemy = Enemy()

    enemies = pygame.sprite.Group()
    enemies.add(enemy)

    while running:
        # SCREEN.fill((255, 255, 255))
        SCREEN.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        enemy.move()
        player.update()

        if pygame.sprite.spritecollideany(player, enemies):
            running = False

        player.draw(SCREEN)
        enemy.draw(SCREEN)

        score_img = font_small.render(str(0), True, (0, 0, 0))
        SCREEN.blit(score_img, (10, 10))

        pygame.display.update()
        CLOCK.tick(30)


if __name__ == '__main__':
    main()