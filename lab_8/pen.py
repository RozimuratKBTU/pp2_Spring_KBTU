import pygame

BLACK = (0, 0, 0)
LINE_COLOR = (50, 50, 50)
HEIGHT = 400
WIDTH = 400

CELL_WIDTH = 20


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        drawGrid()
        drawSnake()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.update()


def drawGrid():
    for x in range(0, WIDTH, CELL_WIDTH):
        for y in range(0, HEIGHT, CELL_WIDTH):
            rect = pygame.Rect(x, y, CELL_WIDTH, CELL_WIDTH)
            pygame.draw.rect(SCREEN, LINE_COLOR, rect, 1)


def drawSnake():
    snake = [(10, 11), (10, 12), (10, 13)]
    #head
    x,y = snake[0]
    rect = pygame.Rect(CELL_WIDTH * x, CELL_WIDTH * y, CELL_WIDTH, CELL_WIDTH)
    pygame.draw.rect(SCREEN, (255, 0, 0), rect)


    for x,y in snake[1:]:
        rect = pygame.Rect(CELL_WIDTH * x, CELL_WIDTH * y, CELL_WIDTH, CELL_WIDTH)
        pygame.draw.rect(SCREEN, (0, 255, 0), rect)



main()
