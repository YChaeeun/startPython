import pygame, sys, random
from pygame.locals import *
import os

pygame.init()

pygame.display.set_caption("rain")
screen = pygame.display.set_mode((1000, 600))

clock = pygame.time.Clock()

raindrop_spawn_time = 0


current_path = os.path.dirname(__file__) # Where your .py file is located
image_path = os.path.join(current_path, 'images') # The image folder path

person_umbrella = pygame.image.load(os.path.join(image_path, 'umbrella.png'))


class Raindrop :
    def __init__(self) :
        self.x = random.randint(0,1000)
        self.y = -5
        self.speed = random.randint(5,12)
    
    def move(self) :
        self.y += self.speed
    
    def draw(self) :
        pygame.draw.line(screen, (0,0,0), (self.x,self.y), (self.x, self.y+15), 2)
        #pygame.draw.line(screen, (153,255,204), (self.x,self.y), (self.x, self.y+15), 2)

    def off_screen(self) :
        return self.y > 800



class Person :
    def __init__(self) :
        # 이미지 좌표
        self.x = 300
        self.y = 400

    def draw(self) :
        # 이미지를 화면에 표시함
        screen.blit(person_umbrella, (self.x, self.y))

    # 충돌감지
    def hit_by(self,raindrop) :  
        # Rect() 가상의 보이지 않는 직사각형을 만들어서 인물 앞에 겹쳐놓음
        # collidepoint() : Rect클래스에 있는 함수. 인자로 받아온 객체 raindrop의 위치를 파라미터로 받는다
        return pygame.Rect(self.x, self.y, 200,200).collidepoint((raindrop.x, raindrop.y))

    


raindrops = list()
person = Person()

while 1 :
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()

    screen.fill((255,255,255))
    #screen.fill((125,125,125))
    person.draw()


    raindrops.append(Raindrop())

    i = 0
    while i < len(raindrops) :
        raindrops[i].move()
        raindrops[i].draw()
        # 충돌감지 조건 추가, 우산을 들고 있는 인물이 비 맞지 않도록 설정
        if raindrops[i].off_screen() or person.hit_by(raindrops[i]):
            del raindrops[i]
            i -= 1
        i += 1

    pygame.display.update()