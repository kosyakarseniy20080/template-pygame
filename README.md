import pygame

WIDTH = 360
HEIGHT = 480
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("[KHL]")
clock = pygame.time.Clock()

running = True
red = 0
green = 0
blue = 0


y = 0
x = 0

colorApple = (255, 150, 100)
x_apple = 100
y_apple = 200





while running:
    clock.tick(FPS)
    screen.fill((red,green,blue))
    
    pygame.draw.rect(screen,(100,50,200),[x,y,100,100] )
    # рисуем яблоко
    pygame.draw.circle(screen,colorApple,[x_apple,y_apple],15)
         
    for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y = y - 10
                    print("Нажали на W")
                if event.key == pygame.K_s:
                    y = y + 10  
                    print("Нажали на S")
                if event.key == pygame.K_a:
                    x = x - 10
                    print("Нажали на A")
                if event.key == pygame.K_d:
                    x = x + 10 
                    print("Нажали на D")
                
    
    
    
    pygame.display.flip()
pygame.quit()
    
