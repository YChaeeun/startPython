import pygame, sys, random, time
from pygame.locals import *
import os

pygame.init()

pygame.display.set_caption("rain")
screen = pygame.display.set_mode((1000, 600))

clock = pygame.time.Clock()

raindrop_spawn_time = 0
last_hit_time = 0   # 비를 맞은 시간 기록


current_path = os.path.dirname(__file__) # Where your .py file is located
image_path = os.path.join(current_path, 'images') # The image folder path

person_umbrella = pygame.image.load(os.path.join(image_path, 'umbrella.png'))
no_umbrella = pygame.image.load(os.path.join(image_path, 'sunny.png'))
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
        if time.time() > last_hit_time +1 :  # 비가 1초 이상 오지 않으면 우산을 안쓴 이미지를 전송
            screen.blit(no_umbrella, (self.x, self.y))
        else :
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

    def move(self) :
        if pressed_keys[K_RIGHT] :
            self.x += 3
        if pressed_keys[K_LEFT] :
            self.x -= 3


raindrops = list()
person = Person()
clouds = Cloud(500,25)

while 1 :
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()

    pressed_keys = pygame.key.get_pressed()

    screen.fill((255,255,255))
    #screen.fill((125,125,125))

    person.draw()
    clouds.draw()
    clouds.rain()
    clouds.move()

    i = 0
    while i < len(raindrops) :
        raindrops[i].move()
        raindrops[i].draw()
        if raindrops[i].off_screen():
            del raindrops[i]
            i -= 1

        elif person.hit_by(raindrops[i]) :
            del raindrops[i]
            last_hit_time = time.time()
            i -= 1
        i += 1

    '''
    # flag를 사용해서 위 while문을 작성할 수도 있음
        while i < len(raindrops) :
        raindrops[i].move()
        raindrops[i].draw()

        flag = False

        if raindrops[i].off_screen():
            flag = True

        if person.hit_by(raindrops[i]) :
            last_hit_time = time.time()
            flag = True

        if flg : 
            del raindrops[i]
            i -= 1

        i += 1

    '''

    pygame.display.update()