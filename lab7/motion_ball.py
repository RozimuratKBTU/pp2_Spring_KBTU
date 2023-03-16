import pygame

# initialize pygame
pygame.init()

# set screen dimensions
screen_width = 500
screen_height = 500

# set screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

# set ball parameters
ball_color = (255, 0, 0)
ball_radius = 25
ball_x = screen_width // 2
ball_y = screen_height // 2

# set background color
background_color = (255, 255, 255)

# set movement variables
move_distance = 20

# game loop
running = True
while running:
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # move ball based on arrow key pressed
            if event.key == pygame.K_UP:
                if ball_y - move_distance >= ball_radius:
                    ball_y -= move_distance
            elif event.key == pygame.K_DOWN:
                if ball_y + move_distance <= screen_height - ball_radius:
                    ball_y += move_distance
            elif event.key == pygame.K_LEFT:
                if ball_x - move_distance >= ball_radius:
                    ball_x -= move_distance
            elif event.key == pygame.K_RIGHT:
                if ball_x + move_distance <= screen_width - ball_radius:
                    ball_x += move_distance

    # draw background
    screen.fill(background_color)

    # draw ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # update screen
    pygame.display.flip()

# quit pygame
pygame.quit()
