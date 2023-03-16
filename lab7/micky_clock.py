
import pygame
from datetime import datetime
import math

RADIUS = 360


def get_clock_pos(clock_dict, clock_hand):
    x = 410 + 300 * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = 410 + 300 * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y


pygame.init()

screen = pygame.display.set_mode((820, 820))
clock = pygame.time.Clock()
clock60 = dict(zip(range(60), range(0, 360, 6)))
font = pygame.font.SysFont('Verdana', 36)
bg = pygame.image.load(r'tsis_7/mic.png').convert()
bg_rect = bg.get_rect()
image_left = pygame.image.load(r"tsis_7/second.png")
left_rect = image_left.get_rect(bottomleft=(415, 565))
image_right = pygame.image.load(r'tsis_7/minute.png')
right_rect = image_right.get_rect(bottomright=(825, 600))

while True:

    screen.blit(bg, bg_rect)


    t = datetime.now()


    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second
    position_minute = get_clock_pos(clock60, minute)


    a = math.atan2(position_minute[1] - (left_rect[1] + 32), position_minute[0] - (left_rect[0] + 26))
    right_hand_rot = pygame.transform.rotate(image_right, 720 - a * 57.29)
    right_rect1 = (right_rect[0] - right_hand_rot.get_rect().width / 2, right_rect[1] - right_hand_rot.get_rect().height / 2)
    screen.blit(right_hand_rot, right_rect1)


    position_second = get_clock_pos(clock60, second)
    angle = math.atan2(position_second[1] - (left_rect[1] + 32), position_second[0] - (left_rect[0] + 26))
    left_hand_rot = pygame.transform.rotate(image_left, 360 - angle * 57.29)
    left_rect1 = (left_rect[0] - left_hand_rot.get_rect().width / 2, left_rect[1] - left_hand_rot.get_rect().height / 2)
    screen.blit(left_hand_rot, left_rect1)
 

 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    t = datetime.now()
    time_render = font.render(f"{t:%H:%M:%S}", True, (25, 100, 100), (255, 255, 255))
    screen.blit(time_render, (0, 0))
    pygame.display.update()
    clock.tick(10)
    screen.fill(0)


