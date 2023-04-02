import pygame
import random
pygame.init()

winWidth = 800
winHeight = 640
win = pygame.display.set_mode((winWidth, winHeight))
bg = pygame.Surface((winWidth, winHeight))  # width,height
road = pygame.Surface((400, winHeight))  # width,height
road.fill((67, 67, 67))
bg.fill((212, 183, 105))  # color

pygame.display.set_caption("Kill Shrek 1")

sprites = []
for i in range(4):
    sprites.append(pygame.image.load(f'anim/shrek_{i}.png'))

# for sp in sprites:
#     sp = pygame.transform.scale(sp, (128, 128))


class GameObject(object):
    def __init__(self, x=10, y=10, color=(255, 255, 255), speed=8):
        self.x = x
        self.y = y
        self.color = color
        self.up = True
        self.down = False
        self.left = False
        self.right = False
        self.speed = speed
        self.hero = False

    def direction(self, right=False, left=False, down=False, up=False):
        self.right = right
        self.left = left
        self.up = up
        self.down = down

    def move(self):
        if self.right:
            self.x += self.speed
        elif self.left:
            self.x -= self.speed

    def fall(self):
        pass


class Rectangle(GameObject):
    def __init__(self, x=10, y=10, color=(255, 255, 255), width=30, height=30, speed=8):
        GameObject.__init__(self, x, y, color)
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.height))
        # hitbox draw
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        # pygame.draw.rect(
        #     win, [0, 255, 0], (self.x, self.y, self.width, self.height), 1)

    def fall(self):
        if not self.hero:
            self.y += self.speed


class Circle(GameObject):
    def __init__(self, x=10, y=10, color=(255, 255, 255), radius=30, speed=8):
        GameObject.__init__(self, x, y, color, speed)
        self.radius = radius
        self.hitbox = pygame.Rect(
            self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)
        self.count = 0

    def draw(self):
        # pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        # hitbox draw
        self.hitbox = pygame.Rect(
            self.x+30, self.y-self.radius, self.radius*2, self.radius*2)

        self.count += 1
        if self.count > 79:
            self.count = 0
        win.blit(pygame.transform.scale(
            sprites[self.count//20], (128, 128)), (self.x-self.radius, self.y-self.radius))
        pygame.draw.rect(
            win, [0, 255, 0], (self.x+30, self.y-self.radius, self.radius*2, self.radius*2), 1)

    def fall(self):
        global score
        if not self.hero:
            self.y += self.speed
        if self.hitbox.colliderect(mainCar.hitbox):
            obstacles.remove(self)
            score += 1


def drawScore():
    global score
    font = pygame.font.SysFont('ComicSans', 30)
    text = font.render(f'Score:{score}', 1, (255, 255, 255))
    win.blit(text, (620, 20))


def winUpdate():
    win.blit(bg, (0, 0))
    win.blit(road, (200, 0))
    print(mainCar.hitbox)
    for l in lines:
        l.draw()
        l.fall()
        if l.y > 600:
            l.y = -200
    for obs in obstacles:
        obs.draw()
    for obs in obstacles:
        obs.fall()
        if obs.y > 700:
            obstacles.remove(obs)
    for t in trees:
        t.draw()
    for t in trees:
        t.fall()
        if t.y > 700:
            trees.remove(t)
    for go in gameObjects:
        go.draw()
        go.fall()
    for go in gameObjects:
        if go.y > 700:
            gameObjects.remove(go)
    drawScore()

    # pygame.draw.circle(win, (255, 0, 0), (400, 400), 50)
    # pygame.draw.circle(win, (0, 255, 0), (600, 400), 50)
    pygame.display.update()


FPS = 60
clock = pygame.time.Clock()
run = True


gameObjects = []
lines = []
obstacles = []
trees = []
score = 0
mainCar = Rectangle(winWidth//2, 540, (171, 11, 11), 32, 64)
mainCar.hero = True
line1 = Rectangle(390, -200, (255, 255, 255), 20, 150, 6)
line2 = Rectangle(390, 0, (255, 255, 255), 20, 150, 6)
line3 = Rectangle(390, 200, (255, 255, 255), 20, 150, 6)
line4 = Rectangle(390, 400, (255, 255, 255), 20, 150, 6)

gameObjects.extend([mainCar])
lines.extend([line1, line2, line3, line4])


def spawner():
    if len(obstacles) < 3:
        obstacles.append(Circle(random.randrange(220, 580, 20), random.randrange(-500, -50, 100), (random.randint(
            100, 130), random.randint(40, 60), random.randint(150, 170)), 16))
    # if len(trees) < 30:
    #     trees.append(Circle(random.randrange(0, 170, 20), random.randrange(-500, -50, 100), (random.randint(
    #         20, 30), random.randint(150, 170), random.randint(25, 50)), random.randrange(20, 40, 10)))
    #     trees.append(Circle(random.randrange(630, 770, 20), random.randrange(-500, -50, 100), (random.randint(
    #         20, 30), random.randint(150, 170), random.randint(25, 50)), random.randrange(20, 40, 10)))


def runProg():
    global run
    while run:
        ms = clock.tick(FPS)  # FPS - fps, ms - millsec between frames
        spawner()
        winUpdate()
        keys = pygame.key.get_pressed()
        # for quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if keys[pygame.K_d] and mainCar.x < winWidth - 200 - mainCar.width:
            mainCar.direction(right=True)
            mainCar.move()
        elif keys[pygame.K_a] and mainCar.x > 200:
            mainCar.direction(left=True)
            mainCar.move()


runProg()
pygame.quit()
