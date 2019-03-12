import pygame, sys, random
from pygame.locals import *

pygame.init()

pygame.display.set_caption("rain")
screen = pygame.display.set_mode((1000, 600))

clock = pygame.time.Clock()

raindrop_spawn_time = 0

class Raindrop :
    def __init__(self) :
        self.x = random.randint(0,1000)
        self.y = -5     # 스크린 밖에서 대기
    
    def move(self) :
        self.y += 7
    
    def draw(self) :
        pygame.draw.line(screen, (255,255,255), (self.x,self.y), (self.x, self.y+15), 1)

raindrops = list()

while 1 :
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()
    screen.fill((125,125,125))

    # 객체 생성 후 리스트에 추가
    raindrops.append(Raindrop())

    # 각 객체들이 함수 실행
    for raindrop in raindrops :
        raindrop.move()
        raindrop.draw()

    pygame.display.update()