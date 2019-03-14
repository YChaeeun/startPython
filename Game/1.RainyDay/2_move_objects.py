import pygame, sys
from pygame.locals import *
pygame.init()
pygame.display.set_caption("First Program")  # 게임 윈도우에 제목 넣기

screen = pygame.display.set_mode((700, 580))

xpos = 50
ypos = 200

# 시계를 설정해서 루프를 도는 시간을 모두 동일하게 설정
clock = pygame.time.Clock()
while 1 :

    clock.tick(150)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_RIGHT]:
        xpos += 2
    if pressed_keys[K_LEFT] :
        xpos -= 2
    if pressed_keys[K_UP]:
        ypos -= 1
    if pressed_keys[K_DOWN] :
        ypos += 2

    screen.fill((255,255,255))

    pygame.draw.circle(screen, (0,255,0), (100, 200), 20, 4)
    pygame.draw.rect(screen,(255,0,0), (xpos,ypos,40,30))
    pygame.display.update()