
import pygame 
import random

# переменные с размерами экрана
WIDTH = 360
HEIGHT = 480
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()
# создаем переменную, в которую запихиваем экранб устанавливаем ширину и высоту
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# заполняю экран белым цветом 
screen.fill(WHITE)
# задаю экрану название
pygame.display.set_caption("[KHL]")
# переменная, которая хранит время обновления экрана
clock = pygame.time.Clock()
# Цикл игры
running = True

screenColor = (0,0,0)
# Параметры игрока
y = 0
x = 0
# ширина и высота игрока
width_player = 50
height_player = 50


colorApple = (255, 150, 100)
x_apple = 100
y_apple = 200





while running:
    # Держим цикл на правильной скорости 
    clock.tick(FPS)
    # заполнить экран цветом
    screen.fill(screenColor)

    # рисуем прямоугольник в screen c цветом (100,50,200) с координатами и размером
    pygame.draw.rect(screen,(100,50,200),[x,y,width_player,height_player] )
    # рисуем яблоко
    pygame.draw.circle(screen,colorApple,[x_apple,y_apple],15)
    if (x<0 or x > WIDTH - 50):
        running = False
        pass
    
    if ((x < x_apple+15  and x < x_apple-15 < x + width_player) and (y < y_apple+15 and y < y_apple-15 < y + height_player)):
        width_player += 10
        x_apple = random.randint(0,WIDTH)
        y_apple = random.randint(0,HEIGHT)
        pygame.draw.circle(screen,colorApple,[x_apple,y_apple],15)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y = y - 10
    if keys[pygame.K_s]:
        y = y + 10  
    if keys[pygame.K_a]:
        x = x - 10
    if keys[pygame.K_d]:
        x = x + 10
    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False      
    

    pygame.display.flip()
pygame.quit()