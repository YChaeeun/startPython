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
        self.y = -5
        self.speed = random.randint(5,12) # 비가 내리는 속도를 다르게 설정
        # 만약 이를 move에 넣으면 비가 내리는 중간중간에도 계속 속도가 달라져
    
    def move(self) :
        self.y += self.speed
    
    def draw(self) :
        pygame.draw.line(screen, (153,255,204), (self.x,self.y), (self.x, self.y+15), 2)

    # 메모리 과부하를 막기 위해 떨어진 후에 빗방울 객체 제거
    def off_screen(self) :
        return self.y > 800

raindrops = list()

while 1 :
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()
    screen.fill((125,125,125))

    raindrops.append(Raindrop())

    i = 0
    while i < len(raindrops) :
        raindrops[i].move()
        raindrops[i].draw()
        if raindrops[i].off_screen() :
            del raindrops[i]
            i -= 1
        i += 1

    pygame.display.update()