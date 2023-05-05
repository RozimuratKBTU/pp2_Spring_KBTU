import pygame
from random import randrange
import psycopg2

print('Введите имя пользователя')
account = input()
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)
cursor = conn.cursor()
cursor.execute('SELECT * FROM snake LIMIT 10')
records = cursor.fetchall()
cursor = conn.cursor()

count = 0
total_score = 0
add_ = True

for row in records:
    if row[0] == account:
        count = row[1]
        total_score = row[2]
        add_ = False
        break

if add_:
    postgres_insert_query = """ INSERT INTO snake (name_,score,total_score) VALUES (%s,%s,%s)"""
    record_to_insert = (account, 0, 0)

    cursor.execute(postgres_insert_query, record_to_insert)
    conn.commit()

pygame.init()
level = 1
mon = 800
size = 50
fps = 60
bg = pygame.image.load("background.jpg")
bg = pygame.transform.scale(bg, (800, 800))

x, y = 300, 300
length = 1
snake = [(x, y)]

buttons = {
    'w': True,
    'a': True,
    'd': True,
    's': True
}

front = pygame.font.SysFont('Ariel', 26, True)

walls = {  # уровни препятствий,
    1: [(50, 50), (50, 100), (50, 150), (50, 200), (150, 0), (200, 0), (250, 0), (500, 500), (550, 500), (500, 550),
        (600, 500), (650, 500)],
    2: [(700, 700), (650, 700), (700, 650), (600, 700), (700, 600), (700, 550), (650, 550), (650, 500)],
    3: [(0, 0), (50, 0), (100, 0), (150, 0), (200, 0), (250, 0), (300, 0), (350, 0), (400, 0), (450, 0), (500, 0),
        (550, 0), (600, 0), (650, 0), (700, 0), (0, 50), (0, 100), (0, 150), (0, 200), (0, 250), (0, 300), (0, 350),
        (0, 400), (0, 450), (0, 500), (0, 550), (0, 600), (0, 650), (0, 700)]
}

speed = 7  # стрость для clock
sup = 10  # для 44,45 а так же для 124 строки нужнo, для range чтобы узнать попадает ли score в range
score = 2  # очки за каждое яблоко
dx, dy = 0, 0  # направление

clock = pygame.time.Clock()
time = 50

apple = randrange(50, mon, size), randrange(0, mon, size)  # спавн яблока
while apple in walls:
    apple = randrange(50, mon, size), randrange(0, mon, size)

level1 = 9  # range
level2 = 20

screen = pygame.display.set_mode([mon, mon])

score_font = pygame.font.SysFont("Verdana", 20)

working = True
while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False

        if event.type == pygame.KEYDOWN:  # полностью движение
            if event.key == pygame.K_w and buttons['w']:
                # если нажали w то змейка будет двигать вверх, ибо dy будет равен -1
                # (тоесть вы будете двигаться по координа dy в минусовыю часть, тоесть вверх)
                # а buttonsp['w'] нужен для того чтобы при движений вниз s  мы не могли двигаться одновременно вверх
                buttons = {
                    'w': True,
                    'a': True,
                    'd': True,
                    's': False
                }
                dx, dy = 0, -1
            elif event.key == pygame.K_s and buttons['s']:
                dx, dy = 0, 1
                buttons = {
                    'w': False,
                    'a': True,
                    'd': True,
                    's': True
                }
            elif event.key == pygame.K_a and buttons['a']:
                dx, dy = -1, 0
                buttons = {
                    'w': True,
                    'a': True,
                    'd': False,
                    's': True
                }
            elif event.key == pygame.K_d and buttons['d']:
                dx, dy = 1, 0
                buttons = {
                    'w': True,
                    'a': False,
                    'd': True,
                    's': True  # sw
                }
            if event.key == pygame.K_q:
                sql_update_query = """Update snake set score = %s where name_ = %s"""
                cursor.execute(sql_update_query, (count, account))
                conn.commit()
                working = False
                count = 0

    screen.blit(bg, (0, 0))  # рисуем задний фон

    if snake[-1] in walls[level]:  # если координаты головы есть в координатах стен то игра останавливается
        total_score += count
        count = 0
        sql_update_query = """Update snake set score = %s where name_ = %s"""
        cursor.execute(sql_update_query, (count, account))
        conn.commit()

        total_score += count
        working = False

    if apple in walls[level]:  # нужна для проверки если яблоко появилось внутри стен
        apple = randrange(50, mon, size), randrange(0, mon, size)

    [(pygame.draw.rect(screen, pygame.Color('blue'), (i, j, size - 2, size - 2))) for i, j in snake]  # рисуем змейку

    pygame.draw.rect(screen, pygame.Color('red'), (*apple, size - 2, size - 2))  # рисуем яблоко

    for i in walls[level]:  # рисуем стены определенного уровня
        pygame.draw.rect(screen, (0, 0, 0), (i[0], i[1], 48, 48))

    render_score = front.render(f'SCORE:{count}', 1, pygame.Color('white'))  # пишем score
    render_score2 = front.render(f'TOTAL_SCORE:{total_score}', 1, pygame.Color('white'))
    screen.blit(render_score, (5, 5))  # рисуем score
    screen.blit(render_score2, (5, 20))

    if time == 0:  # время для случая, если время для сьедания яблока истекло
        apple = randrange(50, mon, size), randrange(0, mon, size)
        time = 50

    x += dx * size  # непрерывное движение
    y += dy * size

    time -= 1  # раз в 50 speed мы обновляем местоположение яблоки, это нужно нам для 111 строки

    snake.append((x, y))  # координаты змейки

    snake = snake[-length:]  # для того чтобы мы брали только змейку, а не места где она прошлась

    if count in range(level1,
                      level2):  # нужна для переноса в след уровень,а так же для увеличения награды за яблоко, скорость,
        level1 += sup
        level2 += sup
        sup += 20
        level += 1
        score += 1
        speed += 2
    if level == 4:
        level = 1

    if snake[-1] == apple:  # в случае если координата яблоки и головы змейки совпала
        count += score
        length += 1
        time = 50
        apple = randrange(50, mon, size), randrange(0, mon, size)

    if x < 0 or x > mon - size or y < 0 or y > mon - size or len(snake) != len(set(snake)):
        # выход за пределы поля или змейка входит в себя
        total_score += count
        count = 0
        sql_update_query = """Update snake set total_score = %s where name_ = %s"""
        cursor.execute(sql_update_query, (count, account))
        conn.commit()
        working = False

    pygame.display.update()
    clock.tick(speed)

total_score += count
sql_update_query = """Update snake set total_score= %s where name_ = %s"""
cursor.execute(sql_update_query, (total_score, account))
conn.commit()

print('Игра завершена!')
cursor.close()
conn.close()