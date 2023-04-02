import random

import pygame

pygame.init()
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
SCORE = 0
clock = pygame.time.Clock()
background = pygame.image.load('./materials/AnimatedStreet.png')
score_font = pygame.font.SysFont("Verdana", 30)
#


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.image = pygame.image.load('./materials/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(self.rect.width, WIDTH - self.rect.width),
            0,
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if self.rect.y > HEIGHT:
            SCORE += 1
            self.speed += 1
            self.rect.center = (
                random.randint(self.rect.width, WIDTH - self.rect.width),
                0,
            )


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load('./materials/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.x - self.speed >= 0:
            self.rect.move_ip(-self.speed, 0)
        elif pressed[pygame.K_RIGHT] and self.rect.x + self.speed + self.rect.width <= WIDTH:
            self.rect.move_ip(self.speed, 0)


def main():
    running = True
    player = Player()
    enemy = Enemy()
    enemies = pygame.sprite.Group()
    enemies.add(enemy)

    while running:
        # SCREEN.fill(WHITE)
        SCREEN.blit(background, (0, 0))
        score = score_font.render(f" Your score: {SCORE}", True, (0, 0, 0))
        SCREEN.blit(score, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update()
        enemy.update()

        player.draw(SCREEN)
        enemy.draw(SCREEN)

        if pygame.sprite.spritecollideany(player, enemies):
            running = False

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()