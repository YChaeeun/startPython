import pygame, sys, random
from pygame.locals import *

pygame.init()
pygame.display.set_caption("rain")

screen = pygame.display.set_mode((1000,600))

clock = pygame.time.Clock()
rain_y = 0
#rain_x = random.randint(0,1000)

rain_x = 300

while 1 :
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()
    screen.fill((125,125,125))

    rain_y += 7

    # screen에 (0,0,0) 색으로, 시작점(rain_x,rain_y)에서  끝나는 지점(rain_x, rain_y+25) 길이 25만큼의 직선을 그림. 직선의 두께는 1로
    pygame.draw.line(screen, (255,255,255), (rain_x,rain_y), (rain_x, rain_y+25), 1)

    pygame.display.update()