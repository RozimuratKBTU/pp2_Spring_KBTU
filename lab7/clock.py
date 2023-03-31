import pygame
import datetime

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


clock = pygame.time.Clock()

WINDOW_SIZE = (800, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Clock")


clock1 = Background('tsis_7/mic.png', (0, 0))

minute_hand_image = pygame.image.load("tsis_7/minute.png").convert_alpha()
second_hand_image = pygame.image.load("tsis_7/second.png").convert_alpha()
MINUTE_HAND_POSITION = (400, 400)
SECOND_HAND_POSITION = (400, 400)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    current_time = datetime.datetime.now().time()

    minute_angle = current_time.minute * 6.0
    minute_hand_image_rotated = pygame.transform.rotate(
        minute_hand_image, -minute_angle)
    minute_hand_rect = minute_hand_image_rotated.get_rect(
        center=MINUTE_HAND_POSITION)

    second_angle = current_time.second * 6.0
    second_hand_image_rotated = pygame.transform.rotate(
        second_hand_image, -second_angle)
    second_hand_rect = second_hand_image_rotated.get_rect(
        center=SECOND_HAND_POSITION)
    
    screen.blit(clock1.image, clock1.rect)
    screen.blit(minute_hand_image_rotated, minute_hand_rect)
    screen.blit(second_hand_image_rotated, second_hand_rect)

    pygame.display.flip()

    clock.tick(60)