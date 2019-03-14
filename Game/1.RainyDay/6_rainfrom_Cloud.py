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
cloud = pygame.image.load(os.path.join(image_path, 'cloud.png'))


class Raindrop :
    def __init__(self,x,y) :
        self.x = x
        self.y = y
        self.speed = random.randint(5,10)
    
    def move(self) :
        self.y += self.speed
    
    def draw(self) :
        pygame.draw.line(screen, (0,0,0), (self.x,self.y), (self.x, self.y+15), 1)
        #pygame.draw.line(screen, (153,255,204), (self.x,self.y), (self.x, self.y+15), 2)

    def off_screen(self) :
        return self.y > 800



class Person :
    def __init__(self) :
        self.x = 300
        self.y = 400

    def draw(self) :
        screen.blit(person_umbrella, (self.x, self.y))

    def hit_by(self,raindrop) :  
        return pygame.Rect(self.x, self.y, 200,200).collidepoint((raindrop.x, raindrop.y))


class Cloud :
    def __init__(self,x, y) :
        self.x = x
        self.y = y

    def draw(self) :
        screen.blit(cloud, (self.x, self.y))

    def rain(self) :
        raindrops.append(Raindrop(random.randint(self.x+50, self.x+175), self.y+150))
        

raindrops = list()
person = Person()
clouds = Cloud(500,25) # 구름 객체 생성 (위치 좌표 x, y)


while 1 :
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()

    screen.fill((255,255,255))
    #screen.fill((125,125,125))
    person.draw()
    clouds.draw()
    clouds.rain()

    i = 0
    while i < len(raindrops) :
        raindrops[i].move()
        raindrops[i].draw()
        if raindrops[i].off_screen() or person.hit_by(raindrops[i]):
            del raindrops[i]
            i -= 1
        i += 1

    pygame.display.update()